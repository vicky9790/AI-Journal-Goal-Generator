import { Component, ElementRef, ViewChild, ChangeDetectorRef, NgZone } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { HttpClient, HttpClientModule } from '@angular/common/http';

@Component({
  selector: 'app-upload',
  standalone: true,
  imports: [CommonModule, FormsModule, HttpClientModule],
  templateUrl: './upload.html',
  styleUrls: ['./upload.css']
})
export class UploadComponent {

  @ViewChild('fileInput') fileInput!: ElementRef<HTMLInputElement>;

  inputText: string = '';
  selectedFile: File | null = null;

  loading = false;
  result: any = null;
  error: string = '';

  constructor(
    private http: HttpClient,
    private cdr: ChangeDetectorRef,
    private zone: NgZone
  ) {}

  onFileSelected(event: any) {
    if (event.target.files.length > 0) {
      this.selectedFile = event.target.files[0];
    }
  }

  submit() {
    if (this.loading) return;

    this.loading = true;
    this.error = '';
    this.result = null;

    if (!this.inputText.trim() && !this.selectedFile) {
      this.error = 'Please type something or upload a file.';
      this.loading = false;
      return;
    }

    const formData = new FormData();

    if (this.inputText.trim()) {
      formData.append('text', this.inputText);
    }

    if (this.selectedFile) {
      formData.append('file', this.selectedFile);
    }

    this.http.post('http://localhost:8000/analyze', formData)
      .subscribe({
        next: (res) => {
          // Ensure UI updates immediately
          this.zone.run(() => {
            this.result = res;
            this.loading = false;
            this.cdr.detectChanges();
          });
        },
        error: (err) => {
          console.error(err);

          this.zone.run(() => {
            this.error = err?.error?.detail || 'Backend error';
            this.loading = false;
            this.cdr.detectChanges();
          });
        }
      });
  }

  clear() {
    this.inputText = '';
    this.selectedFile = null;
    this.result = null;
    this.error = '';
    this.loading = false;

    if (this.fileInput) {
      this.fileInput.nativeElement.value = '';
    }

    this.cdr.detectChanges();
  }
}