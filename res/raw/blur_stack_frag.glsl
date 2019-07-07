// 径向模糊，绘制速度优于高斯模糊，效果接近高斯模糊
precision mediump float;

varying vec2 vTextureCoord;
uniform sampler2D sTexture;
uniform int uBlurLevel;// 范围 0 ~ 25，如果要求更高的效果，推荐先将 Texture 缩小一定倍数再处理。
uniform float uWidthOffset;
uniform float uHeightOffset;

void main (){
    int diameter = 2 * uBlurLevel + 1;
    vec4 sampleTex;
    vec3 col;

    float weightSum = 0.0;
    for (int i = 0; i < diameter; i++) {
        vec2 offset = vec2(float(i - uBlurLevel) * uWidthOffset, float(i - uBlurLevel) * uHeightOffset);
        sampleTex = vec4(texture2D(sTexture, vTextureCoord.st+offset));
        float index = float(i);
        float boxWeight = float(uBlurLevel) + 1.0 - abs(index - float(uBlurLevel));
        col += sampleTex.rgb * boxWeight;
        weightSum += boxWeight;
    }

    gl_FragColor = vec4(col / weightSum, sampleTex.a);
}