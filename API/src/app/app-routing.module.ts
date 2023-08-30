import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { RegistraionComponent } from './registraion/registraion.component';
import { LoginComponent } from './login/login.component';

const routes: Routes = [

  {path: '', redirectTo: 'login', pathMatch: 'full'},
  {path: 'login', component: LoginComponent,



 
},
  {path: 'Registration', component: RegistraionComponent},

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }



export const myRouters =[
  RegistraionComponent,
  LoginComponent,

]