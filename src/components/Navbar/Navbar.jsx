import React from 'react'

import './Navbar.css';

const Navbar = () => {
    return ( 
        <nav className="navbar navbar-expand-lg">
            <div className="container-fluid">
                <a 
                    className="navbar-brand" 
                    href="https://www.mckinsey.com/es"
                    target="_blank"
                    rel="noopener noreferrer"            
                >
                    McKensey HotSpots
                </a>
            </div>
        </nav>
    );
}
 
export default Navbar;