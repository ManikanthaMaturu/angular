import { ChangeDetectorRef, Component } from '@angular/core';
import { AppserviceService } from '../appservice.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent {

  UserName: any;
  Password: any;

  loginResponseMessage: any;
  userdetails: any
  data: any;
  succcessmessage: any;
  userid: any;

  displayName='login';
  email: any;
  result: any;



  constructor(private AppserviceService: AppserviceService, private cdr: ChangeDetectorRef) {}


  ngOnInit() {
    if (this.AppserviceService) {}
  }

  logindetails() {


          const loginData = {
            UserName : this.UserName,
            Password : this.Password
          };


    this.AppserviceService.userlogin(loginData).subscribe(
      (data: any) => {
        
        if (data['Status'] === 200) {
          this.loginResponseMessage = data['Result'] ;

          this.userid = data['Result']['id'];

          this.email = data['Result']['Email']
          console.log("login")
          
          this.succcessmessage = 'Login successful!';
          this.view();
        } 
        else {
          this.loginResponseMessage = 'Username or Password Inccorect';
          this.succcessmessage = 'Login Fail!'
        }
      },
      
      (error: any) => {
        console.error(error);
        this.loginResponseMessage = 'Internal Error'
      }
      

    )
    }


  UserRegDetails() {
    this.AppserviceService.getUser(this.userid).subscribe(
      (userDetails:
         any) => {
          console.log(userDetails.Result)
        this.result = userDetails.Result;
               
        
        console.log(this.result.Password);
        
      },
      (error: any) => {
        console.error('Error fetching user data:', error);
      }

      
    );
    //     } else {
    //       this.loginResponseMessage = 'failed'; // Set an appropriate message for other cases
    //      }
    //   },
    //   (error: any) => {
    //     console.error(error);
    //     this.loginResponseMessage = 'An error occurred';
    //   }
    // );
    


    

  }



  


  view() {
    this.displayName = 'view';
  }


  UserProfile() {
    this.displayName = 'UserProfile';
    this.UserRegDetails();
  }




}
