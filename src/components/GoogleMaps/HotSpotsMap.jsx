import React from 'react';
import { withScriptjs, withGoogleMap, GoogleMap, OverlayView } from 'react-google-maps';

import './HotSpotsMap.css';

const HotSpotsMap = ({position}) => {

    const { latitude, longitude } = position.coords.latitude;

    return ( 

        <GoogleMap
            defaultZoom={10}
            defaultCenter={{ lat: position.coords.latitude, lng: position.coords.longitude}}
        >
            <OverlayView
                mapPaneName={OverlayView.OVERLAY_LAYER}
                position={{ lat: 41.390205, lng: 2.154007}}
                // getPixelPositionOffset={}
            >
                <div className="infobox">
                    <div className="info-message text-center">
                        &#9888; HotSpots
                    </div>
                </div>
            </OverlayView>
            {/* <Marker position={{ lat: 47.444, lng: -122.176}} /> */}

        </GoogleMap>
    );
}
 
export default withScriptjs(withGoogleMap(HotSpotsMap));
