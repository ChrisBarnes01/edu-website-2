import React, { Component } from "react";
import Card from 'react-bootstrap/Card';
import CardColumns from 'react-bootstrap/CardColumns'
import axios from 'axios';
import ClimbingBoxLoader from "react-spinners/ClimbingBoxLoader"

class Home extends Component {
  constructor() {
    super()
    this.state = {
      isLoaded: false,
      projects: [],
    };
  }

  componentDidMount() {
    axios.get("http://127.0.0.1:5000/getallprojects")
    .then(results => {
      console.log(results.data['projects'])
      return results.data['projects'];
    }).then(data => {
      let projects = data.map((proj) =>{
        return(
          <Card>
                <Card.Img variant="top" src={proj['image']}/>
                <Card.Body>
                <Card.Title>{proj['project_name']}</Card.Title>

                <Card.Text>
                  {proj['description']}
                </Card.Text>
                </Card.Body>
          </Card>
        )
      })
      this.setState({projects: projects})
      this.setState({isLoaded: true})
    })
  }

  render() {
    const { isLoaded, projects } = this.state;

    return (
  
        isLoaded?
          (<div>
            <h2>Projects</h2>
            <br></br>
            <p>Here are the Curriculum Projects offered by CS+SocialGood</p>
            <CardColumns>
              {this.state.projects}
            </CardColumns>
         </div>):
         <div>
          <ClimbingBoxLoader/>

         </div>
      
    );
  }
}
 
export default Home;