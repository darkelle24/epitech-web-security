import { Component, OnDestroy, OnInit } from '@angular/core';
import { MatSnackBar } from '@angular/material/snack-bar';
import { Router } from '@angular/router';
import { FileLinkComponent } from './file-link/file-link.component';

@Component({
  selector: 'app-file-list',
  templateUrl: './file-list.component.html',
  styleUrls: ['./file-list.component.scss']
})
export class FileListComponent implements OnInit, OnDestroy {

  list: any[] = [{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}]

  constructor(private _snackBar: MatSnackBar, private router: Router) { }

  ngOnInit(): void {
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
