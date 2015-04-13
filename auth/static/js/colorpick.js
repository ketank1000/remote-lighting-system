/**
 *
 * HTML5 Color Picker
 *
 * Licensed under the MIT license.
 * http://www.opensource.org/licenses/mit-license.php
 * 
 * Copyright 2012, Script Tutorials
 * http://www.script-tutorials.com/
 */

    var bCanPreview = true; // can preview

    // create canvas and context objects
    var canvas = document.getElementById('picker');
    var ctxpic = canvas.getContext('2d');

    // drawing active image
    var image = new Image();
    image.onload = function () {
        ctxpic.drawImage(image, 0, 0, image.width, image.height); // draw the image on the canvas
    }

    // select desired colorwheel
    var imageSrc = "{{ MEDIA_URL }}images/colorwheel2.png";

    
    image.src = imageSrc;

    $('#picker').mousemove(function(e) { // mouse move handler
        if (bCanPreview) {
            // get coordinates of current position
            var canvasOffset = $(canvas).offset();
            var canvasX = Math.floor(e.pageX - canvasOffset.left);
            var canvasY = Math.floor(e.pageY - canvasOffset.top);

            // get current pixel
            var imageData = ctxpic.getImageData(canvasX, canvasY, 1, 1);
            var pixel = imageData.data;

            // update preview color
            pixelColor = "rgb("+pixel[0]+", "+pixel[1]+", "+pixel[2]+")";
            $('.preview').css('backgroundColor', pixelColor);

            // update controls
            $('#rVal').val(pixel[0]);
            $('#gVal').val(pixel[1]);
            $('#bVal').val(pixel[2]);
            $('#rgbVal').val(pixel[0]+','+pixel[1]+','+pixel[2]);

            var dColor = pixel[2] + 256 * pixel[1] + 65536 * pixel[0];
            $('#hexVal').val('#' + ('0000' + dColor.toString(16)).substr(-6));
        }
    });
    $('#picker').click(function(e) { // click event handler
        bCanPreview = !bCanPreview;
    }); 
    $('.preview').click(function(e) { // preview click
        $('.colorpicker').fadeToggle("fast", "linear");
        bCanPreview = true;        
    });