// By Simon Sarris
// www.simonsarris.com
// sarris@acm.org
//
// Last update December 2011
//
// Free to use and distribute at will
// So long as you are nice to people, etc

var del=0;
var ledcount=0;
var str1=null;
var str2=null;
var delcheck=0;
var tempx=0;
var tempy=0;
var flag1=0;
var gr_name=null;
var gr_color=null;
// Constructor for Shape objects to hold data for all drawn objects.
// For now they will just be defined as rectangles.
function Shape(x, y, w, h,status, fill) {
  // This is a very simple and unsafe constructor. All we're doing is checking if the values exist.
  // "x || 0" just means "if there is a value for x, use that. Otherwise use 0."
  // But we aren't checking anything else! We could put "Lalala" for the value of x 
  this.x = x || 0;
  this.y = y || 0;
  this.w = w || 1;
  this.h = h || 1;
  this.r = 15;
  this.lightstatus = status || 0;
  this.ledname = str2;
  this.fill = fill || '#AAAAAA';
}

// Draws this shape to a given context
Shape.prototype.draw = function(ctx) {
 if (this.lightstatus) {     
          
          ctx.fillCircle(this.x, this.y, this.r+5, "yellow");       
      
      } 
  //ctx.fillRect(this.x-15, this.y-15, this.w, this.h);
  ctx.fillStyle = this.fill; //red;
  ctx.beginPath();
  ctx.arc(this.x ,this.y ,this.r,0,Math.PI*2,true);
  ctx.fill();

      ctx.fillCircle = function(x, y, radius, fillColor) {
            this.fillStyle = fillColor;
            this.beginPath();
            this.moveTo(x, y);
            this.arc(x, y, radius, 0, Math.PI * 2, false);
            this.fill();
            
        };



}

// Determine if a point is inside the shape's bounds
Shape.prototype.contains = function(mx, my) {
  // All we have to do is make sure the Mouse X,Y fall in the area between
  // the shape's X and (X + Height) and its Y and (Y + Height)
  return  (this.x-15 <= mx) && (this.x-15 + this.w >= mx) &&
          (this.y-15 <= my) && (this.y-15 + this.h >= my);
}

function CanvasState(canvas) {
  // **** First some setup! ****
  
  this.canvas = canvas;
  this.width = canvas.width;
  this.height = canvas.height;
  this.ctx = canvas.getContext('2d');
  // This complicates things a little but but fixes mouse co-ordinate problems
  // when there's a border or padding. See getMouse for more detail
  var stylePaddingLeft, stylePaddingTop, styleBorderLeft, styleBorderTop;
  if (document.defaultView && document.defaultView.getComputedStyle) {
    this.stylePaddingLeft = parseInt(document.defaultView.getComputedStyle(canvas, null)['paddingLeft'], 10)      || 0;
    this.stylePaddingTop  = parseInt(document.defaultView.getComputedStyle(canvas, null)['paddingTop'], 10)       || 0;
    this.styleBorderLeft  = parseInt(document.defaultView.getComputedStyle(canvas, null)['borderLeftWidth'], 10)  || 0;
    this.styleBorderTop   = parseInt(document.defaultView.getComputedStyle(canvas, null)['borderTopWidth'], 10)   || 0;
  }
  // Some pages have fixed-position bars (like the stumbleupon bar) at the top or left of the page
  // They will mess up mouse coordinates and this fixes that
  var html = document.body.parentNode;
  this.htmlTop = html.offsetTop;
  this.htmlLeft = html.offsetLeft;

  // **** Keep track of state! ****
  
  this.valid = false; // when set to false, the canvas will redraw everything
  this.shapes = [];  // the collection of things to be drawn
  this.dragging = false; // Keep track of when we are dragging
  // the current selected object. In the future we could turn this into an array for multiple selection
  this.selection = null;
  this.dragoffx = 0; // See mousedown and mousemove events for explanation
  this.dragoffy = 0;
  var delcel;
  
  // **** Then events! ****
  
  // This is an example of a closure!
  // Right here "this" means the CanvasState. But we are making events on the Canvas itself,
  // and when the events are fired on the canvas the variable "this" is going to mean the canvas!
  // Since we still want to use this particular CanvasState in the events we have to save a reference to it.
  // This is our reference!
  var myState = this;
  
  //fixes a problem where double clicking causes text to get selected on the canvas
  canvas.addEventListener('selectstart', function(e) { e.preventDefault(); return false; }, false);
  // Up, down, and move are for dragging
  canvas.addEventListener('mousedown', function(e) {
    var mouse = myState.getMouse(e);
    var mx = mouse.x;
    var my = mouse.y;
    var shapes = myState.shapes;
    var l = shapes.length;
    for (var i = l-1; i >= 0; i--) {
      if (shapes[i].contains(mx, my)) {
        var mySel = shapes[i];
        delcel = i;
        // Keep track of where in the object we clicked
        // so we can move it smoothly (see mousemove)
        myState.dragoffx = mx - mySel.x;
        myState.dragoffy = my - mySel.y;
        myState.dragging = true;
        myState.selection = mySel;
        myState.valid = false;


if (flag1==0) {
if (delcheck==0) {
    document.getElementById("FirstName").value = mySel.ledname;
  document.getElementById("xposition").value = mySel.x;
  document.getElementById("yposition").value = mySel.y;
  document.getElementById("status").value = mySel.lightstatus;
  //document.getElementById("fill").value = gr_color;
  document.getElementById("grname").value = gr_name;
  
  };
  if (delcheck==1) {
    delcheck=0;
    document.getElementById("FirstName").value = mySel.ledname;
  document.getElementById("xposition").value = 0;
  document.getElementById("yposition").value = 0;
  document.getElementById("status").value = mySel.lightstatus;
  //document.getElementById("fill").value = gr_color;
  document.getElementById("grname").value = gr_name;
  };

  };

  toggle(mySel.x,mySel.y,mySel.ledname);        
  

        return;
      }
    }
    // havent returned means we have failed to select anything.
    // If there was an object selected, we deselect it
    if (myState.selection) {
      myState.selection = null;
      myState.valid = false; // Need to clear the old selection border
    }
  }, true);
 
  canvas.addEventListener('mouseup', function(e) {
    myState.dragging = false;
    
  }, true);
  // double click for making new shapes
 // canvas.addEventListener('dblclick', function(e) {
  //  var mouse = myState.getMouse(e);
 //   myState.addShape(new Shape(mouse.x , mouse.y , 30, 30, 'rgba(0,255,0,.6)'));
 // }, true);
  
  // **** Options! ****
  
  this.selectionColor = '#CC0000';
  this.selectionWidth = 2;  
  this.interval = 30;
  setInterval(function() { myState.draw(); }, myState.interval);
}

CanvasState.prototype.addShape = function(shape) {
  this.shapes.push(shape);
  this.valid = false;
}

CanvasState.prototype.clear = function() {
  this.ctx.clearRect(0, 0, this.width, this.height);
  //this.ctx.clearRect(0, 0, 15, 15);
}

var temp;
// While draw is called as often as the INTERVAL variable demands,
// It only ever does something if the canvas gets invalidated by our code
CanvasState.prototype.draw = function() {
  // if our state is invalid, redraw and validate!
  if (!this.valid) {
    var ctx = this.ctx;
    var shapes = this.shapes;
    this.clear();
    
    // ** Add stuff you want drawn in the background all the time here **
    
    // draw all shapes
    var l = shapes.length;
    for (var i = 0; i < l; i++) {
      var shape = shapes[i];
      // We can skip the drawing of elements that have moved off the screen:
      if (shape.x > this.width || shape.y > this.height ||
          shape.x + shape.w < 0 || shape.y + shape.h < 0) continue;
      shapes[i].draw(ctx);
    }
    
    // draw selection
    // right now this is just a stroke along the edge of the selected Shape
    if (this.selection != null) {
      var ctx = this.ctx;
      ctx.strokeStyle = this.selectionColor;
      ctx.lineWidth = this.selectionWidth;
      var mySel = this.selection;
      temp = mySel;
      ctx.strokeRect(mySel.x -15,mySel.y -15 ,mySel.w,mySel.h);

      if (del==1) {
        del=0;
        
        mySel.x=0;
        mySel.y=0;
        mySel.w=0;
        mySel.h=0;
        mySel.r=0;
        mySel.shapes.draw(ctx);
        toggle(200,200,mySel.FirstName);

      };

      if (chcolor == 1) {
        chcolor=0;
        mySel.fill = pixelColor;
        mySel.shapes.draw(ctx);
      };
      
    }
    
    // ** Add stuff you want drawn on top all the time here **
    
    this.valid = true;
  }
}


// Creates an object with x and y defined, set to the mouse position relative to the state's canvas
// If you wanna be super-correct this can be tricky, we have to worry about padding and borders
CanvasState.prototype.getMouse = function(e) {
  var element = this.canvas, offsetX = 0, offsetY = 0, mx, my;
  
  // Compute the total offset
  if (element.offsetParent !== undefined) {
    do {
      offsetX += element.offsetLeft;
      offsetY += element.offsetTop;
    } while ((element = element.offsetParent));
  }

  // Add padding and border style widths to offset
  // Also add the <html> offsets in case there's a position:fixed bar
  offsetX += this.stylePaddingLeft + this.styleBorderLeft + this.htmlLeft;
  offsetY += this.stylePaddingTop + this.styleBorderTop + this.htmlTop;

  mx = e.pageX - offsetX;
  my = e.pageY - offsetY;
  
  // We return a simple javascript object (a hash) with x and y defined
  return {x: mx, y: my};
}

// If you dont want to use <body onLoad='init()'>
// You could uncomment this init() reference and place the script reference inside the body tag
//init();
var s = new CanvasState(document.getElementById('canvas1'));
function init() {
  

  ledcount++;
  str1=ledcount.toString();
        str2=str1.concat("s")
    s.addShape(new Shape(40,40,30,30)); // The default is gray
  
  ledcount++;
  str1=ledcount.toString();
        str2=str1.concat("s")
  s.addShape(new Shape(160,140,30,30, 'lightskyblue'));
  // Lets make some partially transparent
  
  ledcount++;
  str1=ledcount.toString();
        str2=str1.concat("s")
  s.addShape(new Shape(280,150,30,30, "blue"));
  
  ledcount++;
  str1=ledcount.toString();
        str2=str1.concat("s")
  s.addShape(new Shape(125,80,30,30, "red"));

  ledcount++;
  str1=ledcount.toString();
        str2=str1.concat("s")
  s.addShape(new Shape(525,380,30,30, "red"));

  ledcount++;
  str1=ledcount.toString();
        str2=str1.concat("s")
  s.addShape(new Shape(325,180,30,30, "#FF0066"));

  ledcount++;
  str1=ledcount.toString();
        str2=str1.concat("s")
  s.addShape(new Shape(425,80,30,30, "#990000"));
  
}

var pixelColor = '#444444';

function adds(){
   

   ledcount++;
   str1=ledcount.toString();
        str2=str1.concat("s")
        toggle(200,200,str2);
    s.addShape(new Shape(200,200,30,30,0, pixelColor));

}
function add1(name,xp,yp,status,fillc){
  ledcount++;
    str2 = name
    s.addShape(new Shape(xp,yp,30,30,status, fillc)); 
    return 0;
}
function delshape(){
  del=1;
  delcheck=1;
 // s.addShape(new Shape(200,200,30,30, pixelColor));

  
}

var chcolor = 0;
function changecolor(){
  chcolor = 1;
}

function toggle(tx,ty,tname) {

  var el = document.getElementById("automation");  
  

  
  if ( el.style.display != 'none' ) {

    if (tempx==tx && tempy==ty) {
    el.style.display = 'none';
    tempx=0;
    tempy=0;
    flag1=0;
  }

  }

  else {
    el.style.left=tx+100+'px';
    el.style.top=ty-10+'px';
    document.getElementById("autoname").innerHTML=tname;
    el.style.display = '';
    tempx=tx;
    tempy=ty;
    flag1=1;

  }

}

function groupdiv(){
  var el = document.getElementById("grdiv");  
  el.style.left=500+'px';
  el.style.top=200+'px';
  el.style.display = '';
}

function grhidediv(){
  gr_name=document.getElementById("groupname").value
  gr_color=document.getElementById("grfill").value
  var el = document.getElementById("grdiv");  
  el.style.display = 'none';
  
}
// Now go make something amazing!