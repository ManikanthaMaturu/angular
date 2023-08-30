import { Component } from '@angular/core';
import { AppserviceService } from '../appservice.service';
import { ChangeDetectorRef } from '@angular/core';


@Component({
  selector: 'app-registraion',
  templateUrl: './registraion.component.html',
  styleUrls: ['./registraion.component.css']
})
export class RegistraionComponent {

  formData: any = {}; // Initialize formData object
  
  UserName:any;
  Email:any;
  Password:any;
 
  registerResponseMessage: any;
  users: any;
  data: any;
  
  constructor( private AppserviceService: AppserviceService, private cdr: ChangeDetectorRef) { }
  ngOnInit(): void {
    if (this.AppserviceService) {
      // this.loadUsers();
    }
  }
  registerdetails(){
    const userData = {
      // unicid: this.unicid,
      UserName: this.UserName,
      Email: this.Email,
      Password: this.Password,
     
    };
    console.log(userData);
    this.AppserviceService.saveuser(userData).subscribe(
      (data:any) => {
      console.log(data);
      if (data['Status'] === 200) {
        this.registerResponseMessage = 'Successfully created';
      } else {
        this.registerResponseMessage = 'User Already Exists'; // Set an appropriate message for other cases
      }
    },
    (error: any) => {
      console.error(error);
      this.registerResponseMessage = 'An error occurred';
    }
    );

  }










  

}
