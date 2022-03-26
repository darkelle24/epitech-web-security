import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import { BehaviorSubject, catchError, map, Observable, of } from 'rxjs';
import { environment } from 'src/environments/environment';
import { ErrorService } from './error.service';

@Injectable({
  providedIn: 'root'
})
export class AuthentificationService {
  private currentUserSubject: BehaviorSubject<any>;

  name = "epitech-web-security"

  urlUser = `${environment.apiUrl}users`

  constructor(private http: HttpClient, private router: Router, private error: ErrorService) {
    // @ts-ignore
    this.currentUserSubject = new BehaviorSubject<any>(JSON.parse(localStorage.getItem(this.name)));
  }

  public get currentUserValue(): any {
    if (environment.authRequired) {
      return this.currentUserSubject.value;
    } else {
      return { username: 'Auth Required Desactivated', id: 0 }
    }
  }

  refreshToken(): Observable<any> {
    return this.http.post<any>(this.urlUser + '/token/refresh', {})
  }

  infoMe(): Observable<any> {
    return this.http.get<any>(this.urlUser + '/me')
  }

  register(email: string, username: string, password: string): Observable<any> {
    return this.http.post<any>(this.urlUser + '/register', { email, username, password })
  }

  login(email: string, password: string): Observable<any> {
    return this.http.post<any>(this.urlUser + '/login', { email: email, password: password })
      .pipe(
        map((user: any) => {
          localStorage.setItem(this.name, JSON.stringify(user));
          this.currentUserSubject.next(user);
          return user;
        }));
  }

  logout(navig: boolean = true): void {
    localStorage.removeItem(this.name);
    // @ts-ignore
    this.currentUserSubject.next(null);
    if (navig)
      this.router.navigate(['login']);
  }


  /* modifyUser(id: number, mail: string, username: string, role: string, group: string | null): Observable<any> {
    return this.http.put<any>(`${environment.apiUrl}users` + '/' + id.toString(), { mail, role, username, group });
  }

  removeUser(id: number): Observable<any> {
    return this.http.delete<any>(`${environment.apiUrl}users` + '/' + id.toString());
  } */
}
