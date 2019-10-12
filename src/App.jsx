import React, { useEffect, useState } from 'react';
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";

import './App.css';
import Navbar from './components/Navbar/Navbar';
import HotSpotsMap from './components/GoogleMaps/HotSpotsMap';

function App() {

  // state
  const [position, setPosition] = useState({});

  const api_key = "AIzaSyCOPK-ekXxUD3OaYo1KMm3CSqeGbPYHHL8";

  useEffect(() => {
    const getLocation = () => {
      navigator.geolocation.getCurrentPosition(setPosition);
    }

    getLocation();
  }, []);
  
  console.log(position);
  

  return (
    <Router>
      <Navbar />

      <div className="container">
        <HotSpotsMap 
          googleMapURL={`https://maps.googleapis.com/maps/api/js?key=${api_key}&v=3.exp&libraries=geometry,drawing,places&region=SP`}
          loadingElement={<div style={{ height: `100%` }} />}
          containerElement={<div style={{ height: `400px` }} />}
          mapElement={<div style={{ height: `100%` }} />} 
          position={position}
        />
      </div>
    </Router>
  );
}

export default App;
