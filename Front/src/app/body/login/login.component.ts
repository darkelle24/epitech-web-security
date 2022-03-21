import { Component, OnInit } from '@angular/core';
import { FormBuilder } from '@angular/forms';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss'],
})
export class LoginComponent implements OnInit {
  constructor(private formBuilder: FormBuilder) {}

  loginForm = this.formBuilder.group({
    email: [''],
    password: [''],
  });

  ngOnInit(): void {}

  onSubmit() {
    console.log(this.loginForm.value);
  }
}
