import React, { Component } from "react";

class Login extends Component {
    render() {
      return (
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

                <button type="submit" className="btn btn-primary btn-block">Submit</button>
                <p className="forgot-password text-right">
                    No Account? <a href="#/signup">Sign Up Here</a>
                </p>
            </form>
      );
    }
  }
   
  export default Login;