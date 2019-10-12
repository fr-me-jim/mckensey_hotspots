import React, { Fragment } from 'react';
import { withScriptjs, withGoogleMap, GoogleMap, OverlayView, Marker } from 'react-google-maps';

import './HotSpotsMap.css';

const HotSpotsMap = ({position}) => {

    // const { latitude, longitude } = position;

    return ( 
        <Fragment>
            <div className="infobox">
                <div className="info-message text-center">
                    &#9888; HotSpots
                </div>
            </div>

            <GoogleMap
                defaultZoom={14}
                defaultCenter={{ lat: position.latitude, lng: position.longitude}}
            >
                <Marker position={{ lat: position.latitude, lng: position.longitude}} />

            </GoogleMap>

        </Fragment>
    );
}
 
export default withScriptjs(withGoogleMap(HotSpotsMap));
