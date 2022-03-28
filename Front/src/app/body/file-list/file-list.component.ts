import { Component, isDevMode, OnDestroy, OnInit } from '@angular/core';
import { MatSnackBar } from '@angular/material/snack-bar';
import { Router } from '@angular/router';
import { ApiService } from 'src/app/_services/api.service';
import { AuthentificationService } from 'src/app/_services/authentification.service';
import { FileLinkComponent } from './file-link/file-link.component';

@Component({
  selector: 'app-file-list',
  templateUrl: './file-list.component.html',
  styleUrls: ['./file-list.component.scss']
})
export class FileListComponent implements OnInit, OnDestroy {
  isLoading: boolean = true

  list: any[] = []

  constructor(private _snackBar: MatSnackBar, private router: Router, private api: ApiService, public auth: AuthentificationService) { }

  ngOnInit(): void {
    this.auth.infoMe().subscribe({
      next: (value: any) => {
        if (isDevMode()) {
          console.log(value)
        }
      },
      error: (err: any) => { }
    })

    this.api.listMyFiles().subscribe({
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

  ngOnDestroy(): void {
    this._snackBar.dismiss()
  }

  openSnackBar(code: string) {
    this._snackBar.openFromComponent(FileLinkComponent, {
      data: { code: code },
      duration: 5000
    });
  }

  goTo(link: string) {
    this.router.navigate([link]);
  }

}
