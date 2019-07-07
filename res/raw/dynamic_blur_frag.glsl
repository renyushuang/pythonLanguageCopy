precision mediump float;
// Android Texture
uniform sampler2D sTexture;
// 模糊等级 >= 0
uniform int uBlurLevel;

varying vec2 vTextureCoord;

vec4 blur(vec2 _uv, sampler2D texture) {
    float disp = 0.;
    float intensity = .2;
    vec4 c1 = vec4(0.0);
    disp = intensity*(0.5-distance(0.5, .1));

    for (int xi=0; xi<uBlurLevel; xi++) {
        float x = float(xi) / float(uBlurLevel) - 0.5;
        for (int yi=0; yi<uBlurLevel; yi++) {
            float y = float(yi) / float(uBlurLevel) - 0.5;
            vec2 v = vec2(x, y);
            float d = disp;
            c1 += texture2D(texture, _uv + d*v);
        }
    }
    c1 /= float(uBlurLevel*uBlurLevel);
    return c1;
}

void main()
{
    if (uBlurLevel == 0){
        gl_FragColor = texture2D(sTexture, vTextureCoord);
    }
    else {
        gl_FragColor = blur(vTextureCoord,sTexture);
    }
}