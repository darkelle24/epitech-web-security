import { Component, isDevMode, OnInit } from '@angular/core';
import { FormControl, Validators } from '@angular/forms';
import { AuthentificationService } from 'src/app/_services/authentification.service';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.scss']
})
export class ProfileComponent implements OnInit {

  hide: boolean = true

  isLoadingEmail: boolean = false
  isLoadingUsername: boolean = false
  isLoadingPassword: boolean = false
  isLoading: boolean = true

  username = new FormControl(undefined, [Validators.required]);
  password = new FormControl(undefined, [Validators.required]);
  email = new FormControl(undefined, [Validators.required]);

  constructor(public auth: AuthentificationService) { }

  ngOnInit(): void {
    this.auth.infoMe().subscribe({
      next: (value: any) => {
        this.isLoading = false
        if (isDevMode()) {
          console.log(value)
        }

        this.email.setValue(value.email)
        this.username.setValue(value.username)
      },
      error: (err: any) => this.isLoading = false
    })
  }

  changeUsername() {
    this.isLoadingUsername = true
    this.auth.modifyUsername(this.username.value).subscribe({
      next: (value: any) => {
        this.isLoadingUsername = false
        if (isDevMode()) {
          console.log(value)
        }
      },
      error: (err: any) => this.isLoadingUsername = false
    })
  }

  changePassword() {
    this.isLoadingPassword = true
    this.auth.modifyPassword(this.password.value).subscribe({
      next: (value: any) => {
        this.isLoadingPassword = false
        if (isDevMode()) {
          console.log(value)
        }
      },
      error: (err: any) => this.isLoadingPassword = false
    })
  }

  changeEmail() {
    this.isLoadingEmail = true
    this.auth.modifyEmail(this.email.value).subscribe({
      next: (value: any) => {
        this.isLoadingEmail = false
        if (isDevMode()) {
          console.log(value)
        }
      },
      error: (err: any) => this.isLoadingEmail = false
    })
  }

  empty() {
    this.isLoading = true
    this.auth.emptyMe().subscribe({
      next: (value: any) => {
        this.isLoading = false
        if (isDevMode()) {
          console.log(value)
        }
      },
      error: (err: any) => this.isLoading = false
    })
  }

  removeMe() {
    this.isLoading = true
    this.auth.removeMe().subscribe({
      next: (value: any) => {
        this.isLoading = false
        if (isDevMode()) {
          console.log(value)
        }
      },
      error: (err: any) => this.isLoading = false
    })
  }

}
