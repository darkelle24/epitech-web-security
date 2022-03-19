import { Component } from '@angular/core';
import { NavigationEnd, Router } from '@angular/router';
import { AuthentificationService } from './_services/authentification.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  loginRegister = true;

  constructor(private router: Router, private auth: AuthentificationService) {
    router.events.subscribe({
      next: (event) => {
        if (event instanceof NavigationEnd) {

          console.log(event);
          if (event.urlAfterRedirects.split('?')[0] === '/login' || event.urlAfterRedirects.split('?')[0] === '/register' || event.urlAfterRedirects.split('?')[0] === '/forgot_password' || event.urlAfterRedirects.split('?')[0] === '/reset_forgot_password') {
            this.loginRegister = true;
          } else {
            this.loginRegister = false;
          }
        }

      }
    });
  }
}
