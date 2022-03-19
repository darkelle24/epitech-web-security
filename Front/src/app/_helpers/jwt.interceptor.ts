import { Injectable } from '@angular/core';
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
import { catchError } from 'rxjs/operators';
import { Router } from '@angular/router';

@Injectable()
export class JwtInterceptor implements HttpInterceptor {

  constructor(private authenticationService: AuthentificationService, private router: Router) { }

  intercept(request: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
    const currentUser = this.authenticationService.currentUserValue;
    const isLoggedIn = currentUser && currentUser.token;
    const isApiUrl = request.url.startsWith(environment.apiUrl);
    const url = this.router.url

    if (isLoggedIn && isApiUrl) {
      request = request.clone({
        setHeaders: {
          Authorization: `Bearer ${currentUser.token}`
        }
      });
    }

    return next.handle(request).pipe(
      catchError((error) => {

        let handled: boolean = false;
        if (error instanceof HttpErrorResponse) {
          if (error.error instanceof ErrorEvent) {
          } else if (url !== '/login') {
            console.log(`error status : ${error.status} ${error.statusText}`);
            switch (error.status) {
              case 401:      //login
                console.log('unauthorized logout')
                this.authenticationService.logout()
                handled = true;
                break;
              case 403:      //login
                console.log('unauthorized logout')
                this.authenticationService.logout()
                handled = true;
                break;
            }
          }
        }

        if (handled) {
          return of(error);
        } else {
          return throwError(() => error);
        }
      })
    );
  }
}
