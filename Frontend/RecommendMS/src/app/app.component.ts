import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})

export class AppComponent implements OnInit{
  title = 'RecommendMS';
  form!: FormGroup;

  constructor(private formBuilder: FormBuilder, private http: HttpClient,) { }

  ngOnInit(): void {
    this.form = this.formBuilder.group({
      genero: [null],
      sentOuTem: [null],
    })
  }

  search(): void {
    console.log(this.form.value);
    //this.http.post('http://localhost:8081/', this.form.value)
    //  .subscribe((res) => {
    //    console.log(res);
    //  });
  }

}
