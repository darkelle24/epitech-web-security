import { Injectable, isDevMode } from '@angular/core';
import {
  HttpRequest,
  HttpHandler,
  HttpEvent,
  HttpInterceptor,
  HttpErrorResponse
} from '@angular/common/http';
import { Observable, of, throwError } from 'rxjs';
import { environment } from '../../environments/environment';
import { AuthentificationService } from '../_services/authentification.service';
import { catchError, map, switchMap } from 'rxjs/operators';
import { Router } from '@angular/router';
import { ErrorService } from '../_services/error.service';

@Injectable()
export class JwtInterceptor implements HttpInterceptor {

  constructor(private authenticationService: AuthentificationService, private router: Router, private error: ErrorService) { }

  intercept(request: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
    const url = this.router.url

    return next.handle(request).pipe(
      catchError((error) => {
        if (error instanceof HttpErrorResponse) {
          if (url !== '/users/login' && error.status === 401) {
            this.handle401Error(request, next);
          } else {
            this.error.showError("Error " + error.status + ": " + error.error.error)
            if (isDevMode()) {
              console.error(error)
            }
          }
        }
        return throwError(() => error);
      })
    );
  }

  private handle401Error(request: HttpRequest<any>, next: HttpHandler) {
    if (this.authenticationService.currentUserValue.refresh_token)
      return this.authenticationService.refreshToken().pipe(
        switchMap((token: any) => {
          return next.handle(this.addTokenHeader(request));
        }),
        catchError((err) => {
          this.authenticationService.logout();
          return throwError(() => err);
        })
      );
    return undefined
  }

  private addTokenHeader(request: HttpRequest<any>) {
    const currentUser = this.authenticationService.currentUserValue;
    const isLoggedIn = currentUser && currentUser.token;
    const isApiUrl = request.url.startsWith(environment.apiUrl);
    const url = this.router.url

    if (isLoggedIn && isApiUrl) {
      if (url === '/users/refresh') {
        request = request.clone({
          setHeaders: {
            Authorization: `Bearer ${currentUser.refresh_token}`
          }
        });
      } else {
        request = request.clone({
          setHeaders: {
            Authorization: `Bearer ${currentUser.access_token}`
          }
        });
      }
    }
    return request
  }
}
