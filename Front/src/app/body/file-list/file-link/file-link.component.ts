import { Component, Inject, OnInit } from '@angular/core';
import { MatSnackBarRef, MAT_SNACK_BAR_DATA } from '@angular/material/snack-bar';
import { ClipboardService } from 'ngx-clipboard';

@Component({
  selector: 'app-file-link',
  templateUrl: './file-link.component.html',
  styleUrls: ['./file-link.component.scss']
})
export class FileLinkComponent {

  constructor(
    public snackBarRef: MatSnackBarRef<FileLinkComponent>,
    private clipboardApi: ClipboardService,
    @Inject(MAT_SNACK_BAR_DATA) public data: any
  ) { }

  copy() {
    this.clipboardApi.copy(this.data.code)
    this.snackBarRef.dismiss()
  }

}
