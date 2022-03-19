import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { AuthGuard } from './_helpers/auth.guard';
import { NoAuthGuard } from './_helpers/no-auth.guard';

import { LoginComponent } from './body/login/login.component';
import { RegisterComponent } from './body/register/register.component';
import { FileListComponent } from './body/file-list/file-list.component';

const routes: Routes = [
  { path: 'login', canActivate: [NoAuthGuard], component: LoginComponent },
  { path: 'register', canActivate: [NoAuthGuard], component: RegisterComponent },

  { path: 'file-list', canActivate: [AuthGuard], component: FileListComponent },

  { path: '', redirectTo: 'file-list', pathMatch: 'full' },
  { path: '**', redirectTo: 'file-list', pathMatch: 'full' }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
