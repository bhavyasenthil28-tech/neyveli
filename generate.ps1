$pages = @(
    "tourist-sights.html", "temples.html", "churches.html", "mosques-dargahs.html",
    "marriage-halls.html", "petrol-bunks.html", "medical-shops.html", "hotels-restaurants.html", "shopping-centers.html",
    "government-offices.html", "hospitals.html", "schools-colleges.html", "public-services.html",
    "transport-bus.html", "transport-railway.html", "transport-local.html", "transport-airport.html"
)

foreach ($page in $pages) {
    $title = $page.Replace("-", " ").Replace(".html", "")
    $title = (Get-Culture).TextInfo.ToTitleCase($title)

    $content = @"
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>$title - NEYVELI Portal</title>
    <link href="https://fonts.googleapis.com/css2?family=Lato:wght@400;700;900&family=Open+Sans:wght@400;600&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="css/style.css">
</head>
<body>
    <header></header>
    <main>
        <div class="breadcrumb">
            <a href="index.html">Home</a> &raquo; <span>$title</span>
        </div>
        <section class="container">
            <h1 class="section-title">$title</h1>
            <p>Welcome to the $title directory. Here you will find detailed information about various locations in Neyveli.</p>
            <div class="grid" style="margin-top: 3rem;">
                <div class="card">
                    <img src="https://images.unsplash.com/photo-1574007624647-7ce854a6bc64?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80" alt="Sample" class="card-img">
                    <div class="card-content">
                        <h3 class="card-title">Sample $title Listing</h3>
                        <p>Location: Neyveli Township</p>
                        <div class="card-action"><a href="#" class="btn-primary" style="font-size:0.8rem; padding:0.5rem 1rem;">View Details</a></div>
                    </div>
                </div>
            </div>
        </section>
    </main>
    <footer></footer>
    <script src="js/main.js"></script>
</body>
</html>
"@
    Set-Content -Path "c:\NEYVELI\$page" -Value $content
}
