import React, { Component } from "react";
import Card from 'react-bootstrap/Card';
import CardColumns from 'react-bootstrap/CardColumns'
 
class Home extends Component {
  render() {
    return (
      <div>
        <h2>Projects</h2>

        
        <br></br>
        <p>Here are the Curriculum Projects offered by CS+SocialGood</p>
 

        <CardColumns>
            <Card>
                <Card.Img variant="top" src="https://res.cloudinary.com/devex/image/fetch/c_scale,f_auto,q_auto,w_720/https://lh6.googleusercontent.com/HqlkUmT5nWr1H-DSn72HFOsVi8IzW1zphpMrzOOSZ7xxo085R3y2V5n-_74NvlAbe4h0CkoR_mq4V-h3aBj2E4qU5dA5HQemqrOSmZrP4GxGADPCdN8hYKpOiSRh3x898nG9UV7m" />
                <Card.Body>
                <Card.Title>Machine Learning International Development</Card.Title>

                <Card.Text>
                Use ML For some really cool stuff!!! We cover the following social topics

                    <li>ML</li>
                    <li>Strings</li>
                </Card.Text>
                </Card.Body>
            </Card>

            <Card>
                <Card.Img variant="top" src="https://nationalpostcom.files.wordpress.com/2014/04/doctors_hospital_corridor_nurse_pushing_gurney_stretcher_bed.jpg?quality=80&strip=all&w=780" />
                <Card.Body>
                <Card.Title>Hospital Database</Card.Title>

                <Card.Text>
                Use ML For some really cool stuff!!! We cover the following social topics

                    <li>Objects</li>
                    <li>Strings</li>
                </Card.Text>
                </Card.Body>
            </Card>

            <Card>
                <Card.Img variant="top" src="https://eesa.lbl.gov/wp-content/uploads/2015/04/IDEAS_coverphoto-720x405.jpg" />
                <Card.Body>
                <Card.Title>Environmental Protection</Card.Title>

                <Card.Text>
                Use ML For some really cool stuff!!! We cover the following social topics

                    <li>Objects</li>
                    <li>Strings</li>
                </Card.Text>
                </Card.Body>
            </Card>

           

        </CardColumns>
      </div>
    );
  }
}
 
export default Home;