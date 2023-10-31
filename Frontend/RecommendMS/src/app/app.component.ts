import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { HttpClient } from '@angular/common/http';
import { RecommendationService } from './service/recommendation.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})

export class AppComponent implements OnInit {
  title = 'RecommendMS';
  form :FormGroup;
  public isModalOpen = false;
  

  public modalContent: any; 

  constructor(private formBuilder: FormBuilder, private http: HttpClient,private recommendationService: RecommendationService) {
    this.form = this.formBuilder.group({
      genero: [null],
      sentOuTem: [null],
    });
   }

  ngOnInit(): void {
    this.form = this.formBuilder.group({
      genero: [null],
      sentOuTem: [null],
    });
  }

  search(): void {
    console.log(this.form.value);


    this.recommendationService
      .getRecommendations(this.form.value.genero, this.form.value.sentOuTem)
      .subscribe((data) => {

        this.showRecommendationsModal(data);
      });
  }

  showRecommendationsModal(data: any): void {
   
    this.isModalOpen = true;
    this.modalContent = data;
  }


  closeModal(): void {
    this.isModalOpen = false;
  }
}
