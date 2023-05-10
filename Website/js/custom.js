// (function($) {
//     "use strict";
//     $(document).ready(function() {
//         $('#nav-expander').on('click', function(e) {
//             e.preventDefault();
//             $('body').toggleClass('nav-expanded');
//         });
//         $('#nav-close').on('click', function(e) {
//             e.preventDefault();
//             $('body').removeClass('nav-expanded');
//         });
//     });

//     $(function() {
//         $('[data-toggle="tooltip"]').tooltip()
//     })

//     $('.carousel').carousel({
//         interval: 4000
//     })

//     $(window).load(function() {
//         $("#preloader").on(500).fadeOut();
//         $(".preloader").on(600).fadeOut("slow");
//     });

//     jQuery(window).scroll(function() {
//         if (jQuery(this).scrollTop() > 1) {
//             jQuery('.dmtop').css({ bottom: "25px" });
//         } else {
//             jQuery('.dmtop').css({ bottom: "-100px" });
//         }
//     });
//     jQuery('.dmtop').click(function() {
//         jQuery('html, body').animate({ scrollTop: '0px' }, 800);
//         return false;
//     });

// })(jQuery);


function openCategory(evt, catName) {
    // Declare all variables
    var i, tabcontent, tablinks;

    // Get all elements with class="tabcontent" and hide them
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }

    // Get all elements with class="tablinks" and remove the class "active"
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }

    // Show the current tab, and add an "active" class to the link that opened the tab
    document.getElementById(catName).style.display = "block";
    evt.currentTarget.className += " active";
}

// 2f949e2487524f1b9ff861b2c95d883b
mainarray = ['Politics', 'Economy', 'Entertainment', 'Tech', 'Sports']

imageArray = []
titleArray = []
const api = 'e70203ab89354eaeb85c51e461950667'


function suna(r, catm) {
    fetch(`https://newsapi.org/v2/everything?q=${mainarray[r]}&apiKey=${api}`).then((apidata) => {
        // console.log(apidata);
        return apidata.json();
    }).then((actualdata) => {
        // console.log(actualdata.articles)
        for (var l = 0; l < 4; l++) {
            var i;
            arrayt = [0, 1, 2, 4, 6, 19, 20, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 55, 56, 57, 58, 59, 60, 61, 62, 63, 65, 66, 67, 69, 70, 71, 72, 73, 74, 75, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
            let randomNumber = Math.floor(
                Math.random() * arrayt.length
            );
            i = arrayt[randomNumber]
            let politics = `
            <div class="col-lg-3 col-md-6 col-sm-12 col-xs-12">
                                                                        <div class="blog-box">
                                                                            <div class="post-media">
                                                                                <a href=${actualdata.articles[i].url} title="">
                                                                                    <img src=${actualdata.articles[i].urlToImage
                                                                                    } alt="" class="img-fluid">
                                                                                    <div class="hovereffect">
                                                                                    </div>
                                                                                    <!-- end hover -->
                                                                                    <span class="menucat">${mainarray[r]}</span>
                                                                                </a>
                                                                            </div>
                                                                            <!-- end media -->
                                                                            <div class="blog-meta">
                                                                                <h4><a href=${actualdata.articles[i].url} title="">${actualdata.articles[i].title}</a></h4>
                                                                            </div>
                                                                            <!-- end meta -->
                                                                        </div>
                                                                        <!-- end blog-box -->
                                                                    </div>
            `
            document.getElementById(catm).innerHTML += politics
            imageArray.push(actualdata.articles[i].urlToImage)
            titleArray.push(actualdata.articles[i].title)
        }
    }).catch((error) => {
        console.log(error);
    });
}
suna(0, 'politics')
suna(1, 'economy')
suna(2, 'entertainment')
suna(3, 'tech')
suna(4, 'Sports')




fetch(`https://newsapi.org/v2/everything?q=${mainarray[0]}&apiKey=${api}`).then((apidatan) => {
    // console.log(apidata);
    return apidatan.json();
}).then((actualdatan) => {
    var i;
    arrayt = [0, 1, 2, 4, 6, 19, 20, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 55, 56, 57, 58, 59, 60, 61, 62, 63, 65, 66, 67, 69, 70, 71, 72, 73, 74, 75, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
    let randomNumber = Math.floor(
        Math.random() * arrayt.length
    );
    i = arrayt[randomNumber]
    let imaget = `
<img src= ${actualdatan.articles[i].urlToImage} style = "width: 100%; height: 300px"  alt="" class="img-fluid">
                            <div class="shadoweffect">
                                <div class="shadow-desc">
                                    <div class="blog-meta">
                                        <span class="bg-orange"><a href=${actualdatan.articles[i].url} title="">Politics</a></span>
                                        <h4><a href=${actualdatan.articles[i].url} title="">${actualdatan.articles[i].title}</a></h4>
                                        <small><a href="tech-single.html" title="">24 July, 2017</a></small>
                                        <small><a href="tech-author.html" title="">by Amanda</a></small>
                                    </div>
                                    <!-- end meta -->
                                </div>
                                <!-- end shadow-desc -->
                            </div>
`
    document.getElementById('image-01').innerHTML += imaget
}).catch((error) => {
    console.log(error);
});


fetch(`https://newsapi.org/v2/everything?q=${mainarray[1]}&apiKey=${api}`).then((apidatal) => {
    // console.log(apidata);
    return apidatal.json();
}).then((actualdatal) => {
    var i;
    arrayt = [0, 1, 2, 4, 6, 19, 20, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 55, 56, 57, 58, 59, 60, 61, 62, 63, 65, 66, 67, 69, 70, 71, 72, 73, 74, 75, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
    let randomNumber = Math.floor(
        Math.random() * arrayt.length
    );
    i = arrayt[randomNumber]
    let imagel = `
<img src= ${actualdatal.articles[i].urlToImage} style = "width: 394px; height: 300px"  alt="" class="img-fluid">
                            <div class="shadoweffect">
                                <div class="shadow-desc">
                                    <div class="blog-meta">
                                        <span class="bg-orange"><a href=${actualdatal.articles[i].url} title="">Entertainment</a></span>
                                        <h4><a href=${actualdatal.articles[i].url} title="">${actualdatal.articles[i].title}</a></h4>
                                        <small><a href="tech-single.html" title="">24 July, 2017</a></small>
                                        <small><a href="tech-author.html" title="">by Amanda</a></small>
                                    </div>
                                    <!-- end meta -->
                                </div>
                                <!-- end shadow-desc -->
                            </div>
`
    document.getElementById('image-02').innerHTML += imagel
}).catch((error) => {
    console.log(error);
});

fetch(`https://newsapi.org/v2/everything?q=${mainarray[3]}&apiKey=${api}`).then((apidatal) => {
    // console.log(apidata);
    return apidatal.json();
}).then((actualdatal) => {
    var i;
    arrayt = [0, 1, 2, 4, 6, 19, 20, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 55, 56, 57, 58, 59, 60, 61, 62, 63, 65, 66, 67, 69, 70, 71, 72, 73, 74, 75, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
    let randomNumber = Math.floor(
        Math.random() * arrayt.length
    );
    i = arrayt[randomNumber]
    let imagel = `
<img src= ${actualdatal.articles[i].urlToImage} style = "width: 394px; height: 300px"  alt="" class="img-fluid">
                            <div class="shadoweffect">
                                <div class="shadow-desc">
                                    <div class="blog-meta">
                                        <span class="bg-orange"><a href=${actualdatal.articles[i].url} title="">Entertainment</a></span>
                                        <h4><a href=${actualdatal.articles[i].url} title="">${actualdatal.articles[i].title}</a></h4>
                                        <small><a href="tech-single.html" title="">24 July, 2017</a></small>
                                        <small><a href="tech-author.html" title="">by Amanda</a></small>
                                    </div>
                                    <!-- end meta -->
                                </div>
                                <!-- end shadow-desc -->
                            </div>
`
    document.getElementById('image-03').innerHTML += imagel
}).catch((error) => {
    console.log(error);
});


// console.log(imageArray)

// console.log(titleArray)
var m;
arr = [0, 1, 2, 3, 4]
let randomNumber = Math.floor(
    Math.random() * arr.length
);
m = arr[randomNumber]


fetch(`https://newsapi.org/v2/everything?q=${mainarray[m]}&apiKey=${api}`).then((apidatal) => {
    // console.log(apidata);
    return apidatal.json();
}).then((actualdatal) => {
    for (var c = 0; c < 11; c++) {
        var i;
        arrayt = [0, 1, 2, 4, 6, 19, 20, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 55, 56, 57, 58, 59, 60, 61, 62, 63, 65, 66, 67, 69, 70, 71, 72, 73, 74, 75, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
        let randomNumber = Math.floor(
            Math.random() * arrayt.length
        );
        i = arrayt[randomNumber]
        let sank = `
        <br>
        <br>
        <div class="blog-box row">
                                <div class="col-md-4">
                                    <div class="post-media">
                                        <a href=${actualdatal.articles[i].url} title="">
                                            <img src=${actualdatal.articles[i].urlToImage} alt="" class="img-fluid">
                                            <div class="hovereffect"></div>
                                        </a>
                                    </div>
                                    <!-- end media -->
                                </div>
                                <!-- end col -->

                                <div class="blog-meta big-meta col-md-8">
                                    <h4><a href=${actualdatal.articles[i].url} title="">${actualdatal.articles[i].title}</a></h4>
                                    <p>${actualdatal.articles[i].description}</a></small>
                                    
                                </div>
                                <!-- end meta -->
                            </div>
                            <!-- end blog-box -->

                            <hr class="invis">
        `
        document.getElementById('main-content').innerHTML += sank
    }
}).catch((error) => {
    console.log(error)
})

var p;
arayt = [0, 1, 2, 3, 4]
let randoNumber = Math.floor(
    Math.random() * arayt.length
);
p = arayt[randoNumber]

fetch(`https://newsapi.org/v2/everything?q=${mainarray[p]}&apiKey=${api}`).then((apidatal) => {
    // console.log(apidata);
    return apidatal.json();
}).then((actualdatal) => {
    for (var c = 0; c < 10; c++) {

        var i;
        arrayt = [0, 1, 2, 4, 6, 19, 20, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 55, 56, 57, 58, 59, 60, 61, 62, 63, 65, 66, 67, 69, 70, 71, 72, 73, 74, 75, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
        let randomNumber = Math.floor(
            Math.random() * arrayt.length
        );
        i = arrayt[randomNumber]
        let sanke = `
    <div class="col-md-6">
        <div class="blog-box">
            <div class="post-media">
                <a href=${actualdatal.articles[i].url} title="">
                    <img src=${actualdatal.articles[i].urlToImage} class="img-fluid">
                    <div class="hovereffect">
                        <span></span>
                    </div>
                    <!-- end hover -->
                </a>
            </div>
            <!-- end media -->
            <div class="blog-meta big-meta">
                 <span class="color-orange"><a href=${actualdatal.articles[i].url} title="">${mainarray[p]}</a></span>
                <h4><a href=${actualdatal.articles[i].url} title="">${actualdatal.articles[i].title}</a></h4>
                <p>${actualdatal.articles[i].description}</p>
            </div>
             <!-- end meta -->
        </div>
        <!-- end blog-box -->
    </div>
    `
        document.getElementById('vedio').innerHTML += sanke
    }

}).catch((error) => {
    console.log(error)
})

var p;
arayt = [0, 1, 2, 3, 4]
let randNumber = Math.floor(
    Math.random() * arayt.length
);
p = arayt[randNumber]

fetch(`https://newsapi.org/v2/everything?q=${mainarray[p]}&apiKey=${api}`).then((apidatal) => {
    // console.log(apidata);
    return apidatal.json();
}).then((actualdatal) => {
    for (var c = 0; c < 11; c++) {
        var i;
        arrayt = [0, 1, 2, 4, 6, 19, 20, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 55, 56, 57, 58, 59, 60, 61, 62, 63, 65, 66, 67, 69, 70, 71, 72, 73, 74, 75, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
        let randomNumber = Math.floor(
            Math.random() * arrayt.length
        );
        i = arrayt[randomNumber]
        let sanke = `
        <div class="blog-box">
                                    <div class="post-media">
                                        <a href=${actualdatal.articles[i].url} title="">
                                            <img src=${actualdatal.articles[i].urlToImage} alt="" class="img-fluid">
                                            <div class="hovereffect">
                                                <span class="videohover"></span>
                                            </div>
                                            <!-- end hover -->
                                        </a>
                                    </div>
                                    <!-- end media -->
                                    <div class="blog-meta big-meta text-center">
                                        <!-- end post-sharing -->
                                        <h4><a href=${actualdatal.articles[i].url} title="">${actualdatal.articles[i].title}
                                        </p>
                                        <small><a href=${actualdatal.articles[i].url} title="">Videos</a></small>
                                    </div>
                                    <!-- end meta -->
                                </div>
                                <hr class="invis">
        `
        document.getElementById('maint').innerHTML += sanke
    }
}).catch((error) => {
    console.log(error)
})