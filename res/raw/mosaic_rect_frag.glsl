// vert 直接使用 DefaultFilter.NO_FILTER_VERTEX_SHADER
precision mediump float;
// Android Texture
uniform sampler2D sTexture;
// 线性纹理
varying vec2 vTextureCoord;

const vec2 texSize = vec2(640., 640.);
const vec2 mosaicSize = vec2(8., 8.);

void main(void){

    vec4 color;
    //float ratio = texSize.y/texSize.x;
    // 将坐标点放大 640 倍
    vec2 xy = vec2(vTextureCoord.x * texSize.x /** ratio */, vTextureCoord.y * texSize.y);
    // 让坐标为 8 的倍数
    vec2 xyMosaic = vec2(floor(xy.x / mosaicSize.x) * mosaicSize.x,
         floor(xy.y / mosaicSize.y) * mosaicSize.y );

    // 第几块mosaic，指定当前顶点对应第几块  mosaic
    vec2 xyFloor = vec2(floor(mod(xy.x, mosaicSize.x)),
                  floor(mod(xy.y, mosaicSize.y)));
    #if 0
    if((xyFloor.x == 0 || xyFloor.y == 0))
    {
      color = vec4(1., 1., 1., 1.);
    }
    else
    #endif
    {
      // 再将坐标点缩小到原始大小
      vec2 uvMosaic = vec2(xyMosaic.x / texSize.x, xyMosaic.y / texSize.y);
      // 通过这一些操作，会将指定坐标点的数据统一移动到某个坐标点
      color = texture2D(sTexture, uvMosaic);
    }

    gl_FragColor = color;
}
