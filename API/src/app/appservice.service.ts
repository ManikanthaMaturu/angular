import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AppserviceService {

  url = 'http://127.0.0.1:8000/app/reg/'

  loginurl = 'http://127.0.0.1:8000/app/UserLogin/'

  // getuser = 'http://127.0.0.1:8000/app/GetReg/1/'
  getuser = 'http://127.0.0.1:8000/app/'

  constructor(private http: HttpClient) { }


  saveuser(userData:  any) {
    return this.http.post(this.url,userData)
  }

  
  userlogin(logindata: any) {
    return this.http.post(this.loginurl, logindata)
  }

  getUser(userId: string): Observable<any> {
    const url = `${this.getuser}GetReg/${userId}/`; // Assuming your API endpoint for fetching user data
    console.log(url)
    return this.http.get(url);
  }
}

