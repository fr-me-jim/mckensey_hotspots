import React, { useEffect, useState } from 'react';
import { useAsync } from "react-async";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import axios from 'axios';

import './App.css';

// components
import Navbar from './components/Navbar/Navbar';
import HotSpotsMap from './components/GoogleMaps/HotSpotsMap';
import Spinner from './components/Spinner/Spinner';

function App() {

  // state
  const [ position, setPosition ] = useState({});
  const [loading, setLoading] = useState(false);
  const [wcondition, setWcondition] = useState(null);

  const api_key_maps = "AIzaSyCOPK-ekXxUD3OaYo1KMm3CSqeGbPYHHL8";
  const api_key_weather = "35fb9b59febb82adc53f76801fc9ed91";

  useEffect( () => {
    const getLocation = () => {
      setLoading(true);
      if(navigator.geolocation)
        navigator.geolocation.getCurrentPosition(updatePosition);
    }

    getLocation();
  }, []);


  const updatePosition = position => {
    
    setPosition(position.coords);
    setLoading(false);
    
    weatherAPI(position.coords);
  }

  const weatherAPI = position => {
    const { latitude, longitude } = position;

    const url = `https://api.openweathermap.org/data/2.5/weather?appid=${api_key_weather}&lat=${latitude}&lon=${longitude}`;

    axios.get(url)
      .then(response => {
          setWeatherCondition(response.data.weather[0].description);
      });
  }

  const setWeatherCondition = weather => {
    switch (weather.toLowerCase()) {

      case "heavy thunderstorm":
        setWcondition(9);
        break;

      case "heavy rain":
        setWcondition(8);
        break;

      case "heavy snow":
        setWcondition(7);
        break;

      case "thunderstorm":
          setWcondition(6);
          break;

      case "mist":
        setWcondition(5);
        break;

      case "snow":
        setWcondition(4);
        break;
        
      case "rain":
          setWcondition(3);
          break;

      case "shower rain":
        setWcondition(2);
        break;

      case "shower rain":
        setWcondition(1);
        break;
    
      default:
        setWcondition(0);
        break;
    }
  }
  
  
  
  var conditionalComp = loading ? <Spinner /> :
     <HotSpotsMap 
        googleMapURL={`https://maps.googleapis.com/maps/api/js?key=${api_key_maps}&v=3.exp&libraries=geometry,drawing,places&region=SP`}
        loadingElement={<div style={{ height: `100%` }} />}
        containerElement={<div style={{ height: `100%`, width: `100%` }} />}
        mapElement={<div style={{ height: `100%` }} />} 
        position={position}
      />

  return (
    <Router>
      <Navbar />

      <div className="container ">
        { conditionalComp }
      </div>
    </Router>
  );
}

export default App;
