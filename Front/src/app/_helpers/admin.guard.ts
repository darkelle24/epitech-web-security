import { Injectable } from '@angular/core';
import { Router, CanActivate, ActivatedRouteSnapshot, RouterStateSnapshot } from '@angular/router';
import { environment } from 'src/environments/environment';

import { AuthentificationService } from '../_services/authentification.service';

@Injectable({
  providedIn: 'root'
})
export class AdminGuard implements CanActivate {
  constructor(
    private router: Router,
    private authenticationService: AuthentificationService
  ) { }

  canActivate(route: ActivatedRouteSnapshot, state: RouterStateSnapshot): boolean {
    if (environment.authRequired) {
      const currentUser = this.authenticationService.currentUserValue;

      if (currentUser !== null && currentUser.role === 'Admin') {
        return true;
      }
      this.router.navigate(['login']);
      return false;
    } else {
      return true;
    }
  }
}
