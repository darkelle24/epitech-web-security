import { Component, isDevMode, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ApiService } from 'src/app/_services/api.service';
import { AuthentificationService } from 'src/app/_services/authentification.service';

@Component({
  selector: 'app-admin-panel',
  templateUrl: './admin-panel.component.html',
  styleUrls: ['./admin-panel.component.scss']
})
export class AdminPanelComponent implements OnInit {
  isLoading: boolean = true

  isLoadingLittle: boolean = false

  list: any[] = []

  constructor(private api: ApiService, private auth: AuthentificationService, private router: Router) { }

  ngOnInit(): void {
    this.api.listUser().subscribe({
      next: (value: any[]) => {
        this.isLoading = false;
        if (isDevMode()) {
          console.log(value)
        }
        this.list = value
      },
      error: (error: any) => {
        this.isLoading = false;
      }
    })
  }

  admin(event: any, user_id: string, item: any) {
    this.isLoadingLittle = true
    if (event.checked) {
      this.api.opUser(user_id).subscribe({
        next: (value: any) => {
          this.isLoadingLittle = false

          if (isDevMode()) {
            console.log(value)
          }
        },
        error: (err: any) => {
          this.isLoadingLittle = false
          item.account.is_admin = false
        }
      })
    } else {
      this.api.deOpUser(user_id).subscribe({
        next: (value: any) => {
          this.isLoadingLittle = false

          if (isDevMode()) {
            console.log(value)
          }
          if (this.auth.currentUserValue.username === item.username) {
            this.router.navigate(["/file-list"]);
          }
        },
        error: (err: any) => {
          this.isLoadingLittle = false
          item.account.is_admin = true
        }
      })
    }
  }

  ban(event: any, user_id: string, item: any) {
    this.isLoadingLittle = true
    if (event.checked) {
      this.api.banUser(user_id).subscribe({
        next: (value: any) => {
          this.isLoadingLittle = false

          if (isDevMode()) {
            console.log(value)
          }
          if (this.auth.currentUserValue.username === item.username) {
            this.router.navigate(["/file-list"]);
          }
        },
        error: (err: any) => {
          this.isLoadingLittle = false
          item.account.is_admin = false
        }
      })
    } else {
      this.api.unBanUser(user_id).subscribe({
        next: (value: any) => {
          this.isLoadingLittle = false

          if (isDevMode()) {
            console.log(value)
          }
        },
        error: (err: any) => {
          this.isLoadingLittle = false
          item.account.is_admin = true
        }
      })
    }
  }

}
