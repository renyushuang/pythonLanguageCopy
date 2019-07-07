// 高斯模糊速度较慢

precision mediump float;

varying vec2 vTextureCoord;
uniform sampler2D sTexture;
uniform int uBlurLevel; // 范围 0 ~ 25，如果要求更高的效果，推荐先将 Texture 缩小一定倍数再处理。
uniform float uWidthOffset;
uniform float uHeightOffset;

mediump float getGaussWeight(mediump float currentPos, mediump float sigma){
    return 1.0 / sigma * exp(-(currentPos * currentPos) / (2.0 * sigma * sigma));
}

void main() {
    int diameter = 2 * uBlurLevel + 1;
    vec4 sampleTex;
    vec3 col;
    float weightSum = 0.0;

    for (int i = 0; i < diameter; i++) {
        vec2 offset = vec2(float(i - uBlurLevel) * uWidthOffset, float(i - uBlurLevel) * uHeightOffset);
        sampleTex = vec4(texture2D(sTexture, vTextureCoord.st+offset));
        float index = float(i);
        float gaussWeight = getGaussWeight(index - float(diameter - 1)/2.0, (float(diameter - 1)/2.0 + 1.0) / 2.0);
        col += sampleTex.rgb * gaussWeight;
        weightSum += gaussWeight;
    }
    gl_FragColor = vec4(col / weightSum, sampleTex.a);
}