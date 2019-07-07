precision mediump float;
// Android Texture
uniform sampler2D sTexture;

varying vec2 vTextureCoord;

vec4 blur(vec2 _uv, sampler2D texture) {
    float disp = 0.;
    float intensity = .3;
    const int passes = 8;
    vec4 c1 = vec4(0.0);
    disp = intensity*(0.5-distance(0.5, .1));

    for (int xi=0; xi<passes; xi++) {
        float x = float(xi) / float(passes) - 0.5;
        for (int yi=0; yi<passes; yi++) {
            float y = float(yi) / float(passes) - 0.5;
            vec2 v = vec2(x, y);
            float d = disp;
            c1 += texture2D(texture, _uv + d*v);
        }
    }
    c1 /= float(passes*passes);
    return c1;
}

void main()
{
    gl_FragColor= blur(vTextureCoord,sTexture);
}
