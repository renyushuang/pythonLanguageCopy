precision mediump float;

uniform sampler2D sTexture;
uniform float s_alpha;
varying vec2 vTextureCoord;

uniform float len;

void main (void){
float TR = 0.866025;
   float x = vTextureCoord.x;
   float y = vTextureCoord.y;
   int wx = int(x/1.5/len);
   int wy = int(y/TR/len);
   vec2 v1, v2, vn;
   if(wx/2 * 2 == wx) {
      if(wy/2 * 2 == wy) {
            v1 = vec2(len*1.5*float(wx), len*TR*float(wy));
            v2 = vec2(len*1.5*float(wx+1), len*TR*float(wy+1));
         } else {
            v1 = vec2(len*1.5*float(wx), len*TR*float(wy+1));
            v2 = vec2(len*1.5*float(wx+1), len*TR*float(wy));
         }
      } else {
      if(wy/2 * 2 == wy) {
         v1 = vec2(len*1.5*float(wx), len*TR*float(wy+1));
         v2 = vec2(len*1.5*float(wx+1), len*TR*float(wy));
         } else {
            v1 = vec2(len*1.5*float(wx), len*TR*float(wy));
            v2 = vec2(len*1.5*float(wx+1), len*TR*float(wy+1));
         }
   }
   float s1 = sqrt( pow(v1.x-x, 2.0) + pow(v1.y-y, 2.0) );
   float s2 = sqrt( pow(v2.x-x, 2.0) + pow(v2.y-y, 2.0) );
   if(s1 < s2)
      vn = v1;
   else
      vn = v2;
   vec4  color = texture2D(sTexture, vn);
   gl_FragColor = vec4(color.rgb, s_alpha);
}