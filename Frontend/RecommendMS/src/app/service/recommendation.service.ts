import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class RecommendationService {
  constructor(private http: HttpClient) {}

  getRecommendations( genero: string, sentimento: string, tema: string): Observable<any> {
    const url = `http://localhost:8000/filmes/recomendar`;
    const data = { genero, sentimento, tema };
    return this.http.post(url, data);
  }
}
