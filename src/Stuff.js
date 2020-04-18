import React, { Component } from "react";
 
class Stuff extends Component {
  render() {
    return (
      <div>
        <form class="centerForm">
          <h3>Create A Project</h3>

          <div className="form-group">
            <label>Curriculum Name</label>
            <input type="text" name="username" className="form-control" placeholder="Enter name" />
          </div>


          <div className="form-group">
            <label>Total Number of Days to Spend</label>
            <input type="text" name="days" className="form-control" placeholder="Number of days" />
          </div>

          <div className="form-group">
            <label>Number of Days to Allocate to Design Thinking</label>
            <select className="form-control">
              <option value="0">0 Days</option>
              <option value="1">1 Day</option>
              <option value="3">3 Days</option>
              <option value="10">10 Days</option>
          </select>
          </div>

          <button type="submit" className="btn btn-primary btn-block">Auto-Generate Curriculum</button>
          <button type="submit" className="btn btn-primary btn-block">Choose Projects</button>
        </form>
      </div>
    );
  }
}
 
export default Stuff;