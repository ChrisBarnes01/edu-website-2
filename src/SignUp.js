import React, { Component } from "react";
 
class SignUp extends Component {
  render() {
    return (
      <form class="centerForm">
                <h3>Sign Up</h3>

                <div className="form-group">
                    <label>Email address</label>
                    <input type="email" className="form-control" placeholder="Enter email" />
                </div>

                <div className="form-group">
                    <label>Password</label>
                    <input type="password" className="form-control" placeholder="Enter password" />
                </div>
                <div className="form-group">
                    <label>Repeat Password</label>
                    <input type="password" className="form-control" placeholder="Enter password" />
                </div>

                <button type="submit" className="btn btn-primary btn-block">Create Account</button>
                <p className="forgot-password text-right">
                    <a href="#/login">Go Back to Sign In</a>
                </p>
            </form>
    );
  }
}
 
export default SignUp;