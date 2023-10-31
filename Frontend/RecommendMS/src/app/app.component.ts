import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { HttpClient } from '@angular/common/http';
import { RecommendationService } from './service/recommendation.service';
import { ModalComponent } from './modal.component';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  form: FormGroup;
  public isModalOpen = false;
  public modalContent: string[] = [];

  constructor(
    private formBuilder: FormBuilder,
    private http: HttpClient,
    private recommendationService: RecommendationService,
  ) {
    this.form = this.formBuilder.group({
      genero: [null],
      sentimento: [null],
      tema: [null],
    });
  }

  search(): void {
    this.recommendationService
      .getRecommendations( this.form.value.genero, this.form.value.sentimento, this.form.value.tema)
      .subscribe((data) => {
        this.showRecommendationsModal(data);
      });
  }

  showRecommendationsModal(data: any): void {
    this.isModalOpen = true;
    this.modalContent = this.extractMovies(data.recommended_movie);
  }

  closeModal(): void {
    this.isModalOpen = false;
  }

  extractMovies(movieString: string): string[] {
    return movieString.split('\n').map((movie) => movie.trim());
  }
}