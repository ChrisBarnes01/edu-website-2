import React, {Redirect, Component } from "react";
import axios from 'axios'

class Login extends Component {
  
    /*We need to make this a global state!*/
    constructor() {
      super()
      this.state = {
        user_id: 0,
      };
    }

    state = {
      redirect: false,
    }

    renderRedirect = () => {
      if (this.state.redirect) {
        return <Redirect to='/target' />
      }
    }

    signin(username, password){
      console.log("Starting pre axios")
      axios.post('http://127.0.0.1:5000/signin', {
        username: username,
        password: password
      })
      .then(function (response) {
        console.log("HELLO!?")
        console.log(response);
        {/*Here we actually need to do a test! */}
        this.setState({redirect: true})
      })
    } 

    handleClick(){
      console.log("I GOT CLICKED!!")
    }

    render() {        
      return (
        <div>
        {this.renderRedirect()}
        <form class="centerForm">
                <h3>Sign In</h3>

                <div className="form-group">
                    <label>Email address</label>
                    <input type="email" className="form-control" placeholder="Enter email" />
                </div>

                <div className="form-group">
                    <label>Password</label>
                    <input type="password" className="form-control" placeholder="Enter password" />
                </div>

                <button onClick={() => this.signin("hello","world")} className="btn btn-primary btn-block">Submit</button>
                <button onClick={() => this.handleClick()} className="btn btn-primary btn-block">Test Click!!!</button>

                <p className="forgot-password text-right">
                    No Account? <a href="#/signup">Sign Up Here</a>
                </p>
            </form>
            </div>
      );
    }
  }
   
  export default Login;