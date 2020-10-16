/*
Author       : Syed Ekram.
Template Name: Jacqueline - Multipurpose/One-Page Business Template
Version      : 1.0
*/

(function($) {
	'use strict';
	
	$(document).ready(function(){
	
	/*START CONTACT MAP JS*/
		var contact = {"lat":"56.130366", "lon":"-106.34677099999999"}; //Change a map coordinate here!
		try {
			$('.map').gmap3({
				action: 'addMarker',
				latLng: [contact.lat, contact.lon],
				map:{
					center: [contact.lat, contact.lon],
					zoom: 5
					},
				},
				{action: 'setOptions', args:[{scrollwheel:false}]}
			);
		} catch(err) {

		}
	   /*END CONTACT MAP JS*/

	}); 	

	
})($);


  

