import React from 'react';
import './Spinner.css';

const Spinner = () => { 

    return (  
        <div id="circle" className="sk-circle">
            <div className="sk-circle1 sk-child first"></div>
            <div className="sk-circle2 sk-child"></div>
            <div className="sk-circle3 sk-child"></div>
            <div className="sk-circle4 sk-child"></div>
            <div className="sk-circle5 sk-child"></div>
            <div className="sk-circle6 sk-child first"></div>
        </div>
    );
    
}
 
export default Spinner;