import React from 'react';
import { useAsync } from "react-async";
import { withScriptjs, withGoogleMap, GoogleMap, OverlayView, Marker } from 'react-google-maps';

import './HotSpotsMap.css';

const HotSpotsMap = ({position}) => {

    // const { latitude, longitude } = position;

    return ( 

        <GoogleMap
            defaultZoom={14}
            defaultCenter={{ lat: position.latitude, lng: position.longitude}}
        >
            <OverlayView
                mapPaneName={OverlayView.OVERLAY_LAYER}
                position={{ lat: position.latitude, lng: position.longitude}}
                // getPixelPositionOffset={}
            >
                <div className="infobox">
                    <div className="info-message text-center">
                        &#9888; HotSpots
                    </div>
                </div>
            </OverlayView>
            <Marker position={{ lat: position.latitude, lng: position.longitude}} />

        </GoogleMap>
    );
}
 
export default withScriptjs(withGoogleMap(HotSpotsMap));
