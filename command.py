
class JavascriptCommand :
    @classmethod
    def clickVideo(self) :
        return 'document.querySelector("video").click();'
    
    @classmethod
    def getVideoLength(self) :
        return 'return document.querySelector("video").duration;'

    @classmethod
    def checkSkipButton(self) :
        return 'return document.querySelector("button[class=' + '\\"' + 'ytp-ad-skip-button ytp-button' + '\\"' + ']");'

    @classmethod
    def checkSkipButton2(self) :
        return 'return document.querySelector("div[class=' + '\\"' + 'ytp-ad-text ytp-ad-preview-text' + '\\"' + ']");' 

    @classmethod
    def clickSkipButton(self) :
        return 'document.querySelector("button[class=' + '\\"' + 'ytp-ad-skip-button ytp-button' + '\\"' + ']").click();'