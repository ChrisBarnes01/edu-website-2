import React, { Component } from "react";

import {
    Route,
    NavLink,
    HashRouter
  } from "react-router-dom";
  import Home from "./Home";
  import Stuff from "./Stuff";
  import SignUp from "./SignUp";
  import Login from "./Login"

class Main extends Component {

  render() {
    return (
        <HashRouter>
        <div>
          <h1>Teach CS for Good - Teacher Profile</h1>
          
          <ul className="header">
            <li><NavLink exact to="/">Home</NavLink></li>
            <li><NavLink to="/login">Login</NavLink></li>
            <li><NavLink to="/stuff">Stuff</NavLink></li>
            <li><NavLink to="/signup">Sign Up</NavLink></li>
          </ul>
          
          <div className="content">
            <Route exact path="/" component={Home}/>
            <Route path ="/login" component={Login}/>
            <Route path="/stuff" component={Stuff}/>
            <Route path="/signup" component={SignUp}/>
          </div>
        </div>
      </HashRouter>
    );
  }
}
 
export default Main;