import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule, HTTP_INTERCEPTORS } from '@angular/common/http';

import { JwtInterceptor } from './_helpers/jwt.interceptor';

import { ClipboardModule } from 'ngx-clipboard';
import { NgxFileDropModule } from 'ngx-file-drop';

import { MatFormFieldModule } from '@angular/material/form-field';
import { MatButtonModule } from '@angular/material/button';
import { MatInputModule } from '@angular/material/input';
import { MatIconModule } from '@angular/material/icon';
import { MatListModule } from '@angular/material/list';
import { MatDividerModule } from '@angular/material/divider';
import { MatSnackBarModule, MAT_SNACK_BAR_DATA } from '@angular/material/snack-bar';
import { MatTooltipModule } from '@angular/material/tooltip';
import { MatCheckboxModule } from '@angular/material/checkbox';
import { MatProgressSpinnerModule } from '@angular/material/progress-spinner';

import { AppRoutingModule, routingComponents } from './app-routing.module';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { LoginComponent } from './body/login/login.component';
import { RegisterComponent } from './body/register/register.component';
import { FileListComponent } from './body/file-list/file-list.component';
import { ProfileComponent } from './body/profile/profile.component';
import { AddFileComponent } from './body/add-file/add-file.component';
import { AdminPanelComponent } from './body/admin-panel/admin-panel.component';
import { HeaderComponent } from './header/header.component';
import { FileLinkComponent } from './body/file-list/file-link/file-link.component';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    RegisterComponent,
    FileListComponent,
    ProfileComponent,
    AddFileComponent,
    AdminPanelComponent,
    HeaderComponent,
    FileLinkComponent
  ],
  entryComponents: [FileLinkComponent],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    HttpClientModule,
    FormsModule,
    ReactiveFormsModule,
    MatFormFieldModule,
    MatButtonModule,
    MatInputModule,
    MatIconModule,
    MatListModule,
    MatDividerModule,
    MatSnackBarModule,
    ClipboardModule,
    MatTooltipModule,
    MatCheckboxModule,
    NgxFileDropModule,
    MatProgressSpinnerModule
  ],
  providers: [{ provide: HTTP_INTERCEPTORS, useClass: JwtInterceptor, multi: true },
  { provide: MAT_SNACK_BAR_DATA, useValue: {} }],
  bootstrap: [AppComponent]
})
export class AppModule {}
