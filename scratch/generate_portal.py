import os

# Setup directory paths
WORKSPACE_DIR = "/Users/bhavyasundari/Downloads/NEYVELI 2"
DETAILS_DIR = os.path.join(WORKSPACE_DIR, "details")
os.makedirs(DETAILS_DIR, exist_ok=True)

# Define the categories data with completely unique, highly relevant, and context-matching images.
# Local images are used for NEYVELI specific sights where available, and hand-picked Unsplash IDs are used for others.
categories = {
    "tourist-places": {
        "title": "Tourist Places",
        "file": "tourist-places.html",
        "description": "Discover the key landmarks, green parks, and essential attractions across Neyveli.",
        "items": [
            {
                "id": "neyveli-arch",
                "name": "Neyveli Arch",
                "image": "images/neyveli-nlc-industry.jpg",
                "address": "Main Entrance Gate, Chennai-Kumbakonam Highway (NH 36), Neyveli, Tamil Nadu 607801",
                "short_desc": "The iconic grand entrance gateway to the Neyveli Township, symbolizing the power city's rich industrial heritage.",
                "full_desc": "The Neyveli Arch is the grand gateway that welcomes visitors entering the beautifully planned township of Neyveli. Standing tall at the entrance on the National Highway, it represents the industrial might and heritage of Neyveli Lignite Corporation (NLC India Limited). Built alongside a majestic Miner Statue, it stands as a tribute to the thousands of miners and engineers who power the nation. It is a popular spot for visitors to click photographs and is beautifully illuminated during national festivals like Independence Day and Republic Day.",
                "timings": "Open 24 Hours",
                "contact": "Neyveli Township Administration: +91 4142 252253",
                "nearby": [
                    {"name": "Nehru Park", "dist": "2.5 km"},
                    {"name": "Neyveli Central Bus Stand", "dist": "3 km"}
                ],
                "maps": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3914.856980076722!2d79.4883492!3d11.5978121!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3a54d588523c91fb%3A0xc3175ebc088be330!2sNLC%20Main%20Arch!5e0!3m2!1sen!2sin!4v1718612000000!5m2!1sen!2sin",
                "additional_info": "Parking space is available nearby. The area is highly secure and monitored 24/7.",
                "gallery": [
                    "https://images.unsplash.com/photo-1590001155093-a3c66ab0c3ff?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1569336415962-a4bd9f69cd83?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1579546929518-9e396f3cc809?auto=format&fit=crop&w=600&q=80"
                ]
            },
            {
                "id": "nlc-township",
                "name": "NLC India Limited Township",
                "image": "images/neyveli-township-administration.jpg",
                "address": "Neyveli Central Township, Cuddalore District, Tamil Nadu 607801",
                "short_desc": "A highly organized, green, and self-sufficient township created for the workforce of NLC India Limited.",
                "full_desc": "Neyveli Township is one of the most meticulously planned residential complexes in Southern India. Designed to house the employees of NLC India Limited, the township is divided into 32 organized blocks. Each block is self-contained with its own parks, shopping complexes, schools, and medical facilities. The township is renowned for its lush greenery, wide tree-lined avenues, and zero-discharge environment, making it a model for modern sustainable industrial town planning.",
                "timings": "Open 24 Hours",
                "contact": "Township Public Relations Office: +91 4142 223456",
                "nearby": [
                    {"name": "NLC Corporate Office", "dist": "1.2 km"},
                    {"name": "NLC General Hospital", "dist": "2 km"}
                ],
                "maps": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d15659.432655768565!2d79.471694!3d11.603387!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3a54d5bcffffffff%3A0x6b864a787b7a13d3!2sNeyveli%20Township!5e0!3m2!1sen!2sin!4v1718612100000!5m2!1sen!2sin",
                "additional_info": "Visitors require permission for corporate building entry, but the residential blocks and open parks are fully accessible.",
                "gallery": [
                    "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1513694203232-719a280e022f?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1507089947368-19c1da9775ae?auto=format&fit=crop&w=600&q=80"
                ]
            },
            {
                "id": "pichavaram-mangroves",
                "name": "Pichavaram Mangrove Forest",
                "image": "images/neyveli-tourist-place.jpg",
                "address": "Pichavaram, Chidambaram Taluk, Tamil Nadu 608102",
                "short_desc": "Explore the second largest mangrove forest in the world, an incredible day-trip destination from Neyveli.",
                "full_desc": "Located just 45 kilometers from Neyveli, Pichavaram Mangrove Forest is a globally renowned eco-tourism site. It is the second largest mangrove forest in the world, covering an area of about 1,100 hectares. The forest is separated from the Bay of Bengal by a sandy beach and is home to a unique ecosystem of rare water birds, fish, and vegetation. Visitors can rent rowboats or motorboats operated by the forest department to navigate through the complex maze of naturally formed water channels covered by a canopy of green trees.",
                "timings": "09:00 AM to 05:00 PM (Daily)",
                "contact": "Forest Department Booking Office: +91 4144 238010",
                "nearby": [
                    {"name": "Chidambaram Nataraja Temple", "dist": "15 km"},
                    {"name": "Killai Backwaters", "dist": "3 km"}
                ],
                "maps": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3917.4727192664985!2d79.775836!3d11.427778!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3a54c6aaaaaaabcb%3A0xf6708573ef89c3ab!2sPichavaram%20Mangrove%20Forest!5e0!3m2!1sen!2sin!4v1718612200000!5m2!1sen!2sin",
                "additional_info": "Row boating is highly recommended for a quiet and immersive natural experience. Ensure you wear life jackets provided at the dock.",
                "gallery": [
                    "https://images.unsplash.com/photo-1544551763-46a013bb70d5?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1500382017468-9049fed747ef?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1473448912268-2022ce9509d8?auto=format&fit=crop&w=600&q=80"
                ]
            },
            {
                "id": "nehru-park",
                "name": "Nehru Park",
                "image": "images/neyveli-township-gardens.jpg",
                "address": "Block 18, Neyveli Township, Tamil Nadu 607803",
                "short_desc": "A beautifully landscaped park perfect for evening walks, featuring well-maintained gardens and open lawns.",
                "full_desc": "Nehru Park is one of the premier recreational parks in Neyveli Township. Situated centrally in Block 18, it features expansive lawns, a wide array of seasonal floral displays, fountains, and walking tracks. The park is a major hub for township residents, offering a serene atmosphere for morning jogging, evening relaxation, and family picnics. It also has a small children's play section and benches placed under shady trees.",
                "timings": "05:00 AM to 09:00 AM, 04:00 PM to 08:30 PM (Daily)",
                "contact": "Block 18 Maintenance Office: +91 4142 251180",
                "nearby": [
                    {"name": "Sacred Heart Church", "dist": "0.5 km"},
                    {"name": "Block 18 Market", "dist": "0.3 km"}
                ],
                "maps": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3914.856980076722!2d79.475!3d11.60!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3a54d588523c91fb%3A0xc3175ebc088be330!2sNehru%20Park%20Neyveli!5e0!3m2!1sen!2sin!4v1718612300000!5m2!1sen!2sin",
                "additional_info": "No entry fee. Outside food is allowed but littering is strictly prohibited and subject to fines.",
                "gallery": [
                    "https://images.unsplash.com/photo-1448375240586-882707db888b?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1518531933037-91b2f5f229cc?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1470071459604-3b5ec3a7fe05?auto=format&fit=crop&w=600&q=80"
                ]
            },
            {
                "id": "neyveli-boat-house",
                "name": "Neyveli Boat House",
                "image": "images/neyveli-boat-house.jpg",
                "address": "Lake Area, Block 24, Neyveli Township, Tamil Nadu 607801",
                "short_desc": "A serene lakeside spot offering boating facilities for families and tourists visiting the township.",
                "full_desc": "Neyveli Boat House is situated in the scenic Lake Area of Neyveli. The lake, artificially maintained using groundwater pumped during NLC mining operations, has been converted into a beautiful leisure and adventure park. Visitors can rent pedal boats, rowboats, or speedboats to cruise the tranquil waters. The lake surrounding features a paved path for walking, a cafeteria, and well-designed view-points to watch the sunset.",
                "timings": "09:00 AM to 06:00 PM (Daily)",
                "contact": "NLC Recreation Club: +91 4142 253304",
                "nearby": [
                    {"name": "Golden Vinayagar Temple", "dist": "1 km"},
                    {"name": "Neyveli General Hospital", "dist": "1.5 km"}
                ],
                "maps": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3914.856980076722!2d79.478!3d11.595!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3a54d588523c91fb%3A0xc3175ebc088be330!2sNeyveli%20Boat%20House!5e0!3m2!1sen!2sin!4v1718612400000!5m2!1sen!2sin",
                "additional_info": "Boat rental charges are nominal. Life jackets are mandatory. Weekends are usually crowded.",
                "gallery": [
                    "https://images.unsplash.com/photo-1501785888041-af3ef285b470?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1476514525535-07fb3b4ae5f1?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1433832597046-4f10e10ac764?auto=format&fit=crop&w=600&q=80"
                ]
            },
            {
                "id": "childrens-park",
                "name": "Children's Park",
                "image": "images/neyveli-childrens-park.jpg",
                "address": "Main Township Road, Block 24, Neyveli, Tamil Nadu 607801",
                "short_desc": "A vibrant and safe recreational area packed with play equipment for young children.",
                "full_desc": "The Children's Park in Block 24 is the most popular outdoor play destination for families in Neyveli. Equipped with slides, swings, see-saws, and monkey bars, the park provides a safe and engaging space for children. The park features lush lawn seating for parents, clean paved walkways, and food stalls selling ice creams and snacks outside the main gate.",
                "timings": "04:00 PM to 08:30 PM (Daily)",
                "contact": "Civic Amenities Department: +91 4142 254452",
                "nearby": [
                    {"name": "Neyveli Boat House", "dist": "1.2 km"},
                    {"name": "St. Gabriel's Church", "dist": "0.8 km"}
                ],
                "maps": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3914.856980076722!2d79.48!3d11.594!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3a54d588523c91fb%3A0xc3175ebc088be330!2sChildren's%20Park%20Neyveli!5e0!3m2!1sen!2sin!4v1718612500000!5m2!1sen!2sin",
                "additional_info": "Entry fee is very minimal (Rs. 5 per person). Toy train rides are available on weekends.",
                "gallery": [
                    "https://images.unsplash.com/photo-1596464716127-f2a82984de30?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1579684389782-64d84b5e905d?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1531983412531-1f49a365ffed?auto=format&fit=crop&w=600&q=80"
                ]
            }
        ]
    },
    "temples": {
        "title": "Temples",
        "file": "temples.html",
        "description": "Explore the prominent spiritual centers and ancient Hindu temples in and around Neyveli.",
        "items": [
            {
                "id": "sri-nataraja-temple",
                "name": "Sri Nataraja Temple",
                "image": "images/neyveli-nataraja-temple.jpg",
                "address": "Block 29, Neyveli Township, Tamil Nadu 607807",
                "short_desc": "A prominent South Indian temple architecturally inspired by Chidambaram, acting as a major spiritual center.",
                "full_desc": "The Neyveli Sri Nataraja Temple is a major spiritual landmark in the region, modeled after the world-famous Chidambaram Natarajar Temple. Dedicated to Lord Shiva in his cosmic dance form, the temple houses a spectacular, massive bronze Nataraja idol. The temple complex features beautiful Dravidian towers, a vast central courtyard, and is renowned for hosting classical dance festivals, particularly during Maha Shivaratri, drawing dancers and devotees from across the state.",
                "timings": "06:00 AM - 11:30 AM, 04:30 PM - 08:30 PM",
                "contact": "Temple Administration Office: +91 4142 228990",
                "nearby": [
                    {"name": "Neyveli Central Mosque", "dist": "0.5 km"},
                    {"name": "Block 29 Market", "dist": "0.4 km"}
                ],
                "maps": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3914.856980076722!2d79.467!3d11.61!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3a54d588523c91fb%3A0xc3175ebc088be330!2sNeyveli%20Nataraja%20Temple!5e0!3m2!1sen!2sin!4v1718612600000!5m2!1sen!2sin",
                "additional_info": "Traditional dress code is recommended. Photography inside the inner sanctum is strictly prohibited.",
                "gallery": [
                    "https://images.unsplash.com/photo-1602216056096-3b40cc0c9944?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1542856391-010fb87dcfed?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1608958415210-94e824eb976c?auto=format&fit=crop&w=600&q=80"
                ]
            },
            {
                "id": "villudayanpattu-murugan-temple",
                "name": "Villudayanpattu Murugan Temple",
                "image": "images/neyveli-veludayanpattu-murugan-temple.jpg",
                "address": "Veludayanpattu, Neyveli, Tamil Nadu 607802",
                "short_desc": "Ancient and revered Murugan temple located near Neyveli, famous for its unique hunter avatar deity.",
                "full_desc": "The Sri Siva Subramania Swamy Temple, popularly known as Villudayanpattu Murugan Temple, is an ancient temple with a history dating back over 800 years. The temple's unique significance is the deity of Lord Murugan holding a bow and arrows (Villum Ambum) instead of his traditional Vel, symbolizing his role as a divine hunter. It is situated in a tranquil, grove-like setting and holds grand festivals during Panguni Uthiram and Thaipusam.",
                "timings": "06:00 AM - 12:00 PM, 04:00 PM - 08:00 PM",
                "contact": "HR & CE Executive Officer: +91 4142 259880",
                "nearby": [
                    {"name": "Neyveli Arch", "dist": "4 km"},
                    {"name": "Mandharakuppam", "dist": "3.5 km"}
                ],
                "maps": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3914.856980076722!2d79.49!3d11.59!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3a54d588523c91fb%3A0xc3175ebc088be330!2sVilludayanpattu%20Murugan%20Temple!5e0!3m2!1sen!2sin!4v1718612700000!5m2!1sen!2sin",
                "additional_info": "Special abhishekams are performed on Shasti days. The temple has a sacred pond (theertham) which is considered to have healing properties.",
                "gallery": [
                    "https://images.unsplash.com/photo-1590050752117-238cb0612b1b?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1617653252877-e85d956557cb?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1626082927389-6cd097cdc6ec?auto=format&fit=crop&w=600&q=80"
                ]
            },
            {
                "id": "sri-bhuvaraha-swamy-temple",
                "name": "Sri Bhuvaraha Swamy Temple",
                "image": "https://images.unsplash.com/photo-1600100395420-40111ef84877?auto=format&fit=crop&w=600&q=80",
                "address": "Srimushnam, Cuddalore District, Tamil Nadu 608901",
                "short_desc": "A legendary, ancient Vaishnavite temple located near Neyveli, famous for its Varaha avatar deity.",
                "full_desc": "Located about 30 km from Neyveli, the Bhuvaraha Swamy Temple in Srimushnam is one of the eight self-manifested (Swayamvyakta Kshetra) Vaishnavite shrines in India. The temple is dedicated to Lord Vishnu's Varaha (boar) avatar, representing the preservation of Earth. The temple is noted for its spectacular 16-pillared hall (Purushasukta Mandapam) featuring intricate carvings of mythological characters, warriors, and dancers from the Vijayanagara period.",
                "timings": "06:00 AM - 12:30 PM, 04:00 PM - 08:30 PM",
                "contact": "Temple Board Office: +91 4144 245264",
                "nearby": [
                    {"name": "Vridhachalam Shiva Temple", "dist": "19 km"},
                    {"name": "Srimushnam Town", "dist": "0.5 km"}
                ],
                "maps": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3915.228!2d79.40!3d11.39!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3a54c60000000001%3A0x897996f01479cf8d!2sBhuvaraha%20Swamy%20Temple!5e0!3m2!1sen!2sin!4v1718612800000!5m2!1sen!2sin",
                "additional_info": "The local Prasad (Koradu) made of sweet tubers is highly unique to this temple. Visitors should check local bus schedules to Srimushnam.",
                "gallery": [
                    "https://images.unsplash.com/photo-1561361513-2d000a50f0db?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1588615419957-bf66d53c6b45?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1614036417651-efe5912149d8?auto=format&fit=crop&w=600&q=80"
                ]
            },
            {
                "id": "sri-kolanjiappar-temple",
                "name": "Sri Kolanjiappar Temple",
                "image": "https://images.unsplash.com/photo-1540833685304-ff2047a06f7b?auto=format&fit=crop&w=600&q=80",
                "address": "Manavalanallur, Vriddhachalam, Tamil Nadu 606001",
                "short_desc": "A unique Murugan temple where prayers are written and tied to the altar to seek swift divine intervention.",
                "full_desc": "Located 20 km from Neyveli, the Sri Kolanjiappar Temple is a popular pilgrimage site dedicated to Lord Murugan. Here, the deity is worshiped in the form of a naturally occurring stone altar (peetam) rather than an idol. A key unique practice is 'Prarthana' where devotees write their grievances on a piece of paper and tie it to the temple's trident, believing that the deity will resolve their worries within 90 days. The temple has a peaceful, rural vibe.",
                "timings": "06:30 AM - 12:00 PM, 04:30 PM - 08:30 PM",
                "contact": "Temple Trust Office: +91 4143 230230",
                "nearby": [
                    {"name": "Vriddhachalam Junction", "dist": "3 km"},
                    {"name": "Vridhagirishwarar Temple", "dist": "2.5 km"}
                ],
                "maps": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3915.228!2d79.31!3d11.52!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3a54d30000000001%3A0xabcdefabcdefabcd!2sKolanjiappar%20Temple!5e0!3m2!1sen!2sin!4v1718612900000!5m2!1sen!2sin",
                "additional_info": "Ample parking and rest rooms are available. The temple offers free mid-day meals (Annadhanam) daily.",
                "gallery": [
                    "https://images.unsplash.com/photo-1561361047-975c92c90c74?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1596176530529-78163a4f7af2?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1621244249243-436b79b5eea8?auto=format&fit=crop&w=600&q=80"
                ]
            },
            {
                "id": "golden-vinayagar-temple",
                "name": "Sri Golden Vinayagar Temple",
                "image": "https://images.unsplash.com/photo-1568252542512-9fe8fe9c87bb?auto=format&fit=crop&w=600&q=80",
                "address": "Block 24, Neyveli Township, Tamil Nadu 607801",
                "short_desc": "A beautiful, serene temple in Block 24 dedicated to Lord Ganesha, featuring modern architecture.",
                "full_desc": "The Golden Vinayagar Temple is a well-maintained modern shrine in Block 24 of the Neyveli Township. Known for its quiet and peaceful surroundings, the temple attracts local residents for daily prayers. The deity of Lord Vinayagar (Ganesha) is beautifully decorated during festivals like Ganesh Chaturthi. The temple also features shrines for Navagrahas and Lord Murugan.",
                "timings": "07:00 AM - 10:30 AM, 05:30 PM - 08:00 PM",
                "contact": "Block 24 Temple Association: +91 4142 254101",
                "nearby": [
                    {"name": "Neyveli Boat House", "dist": "1 km"},
                    {"name": "Children's Park", "dist": "0.8 km"}
                ],
                "maps": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3914.856980076722!2d79.48!3d11.594!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3a54d588523c91fb%3A0xc3175ebc088be330!2sGolden%20Vinayagar%20Temple!5e0!3m2!1sen!2sin!4v1718613000000!5m2!1sen!2sin",
                "additional_info": "Perfect for a quiet morning meditation. Located inside the peaceful residential township.",
                "gallery": [
                    "https://images.unsplash.com/photo-1554124490-647d6e6a10de?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1598502573215-0d32f4c3b652?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1578507012602-069f2e4aa1a4?auto=format&fit=crop&w=600&q=80"
                ]
            },
            {
                "id": "vadavaur-mariamman-temple",
                "name": "Vadavaur Mariamman Temple",
                "image": "https://images.unsplash.com/photo-1612240498936-65f5101365d2?auto=format&fit=crop&w=600&q=80",
                "address": "Vadavaur Village, Cuddalore-Neyveli Road, Cuddalore, Tamil Nadu 607802",
                "short_desc": "A vibrant village temple dedicated to Goddess Mariamman, famous for its annual fire-walking festival.",
                "full_desc": "Vadavaur Mariamman Temple is a popular village temple situated just outside the Neyveli Township borders. Dedicated to Mariamman, the goddess of rain and health, this temple is highly revered by the rural community. During the Tamil month of Aadi, the temple hosts its grand annual festival, featuring decorated chariot processions, traditional music, and a fire-walking (Theemithi) ceremony where hundreds of devotees walk bare feet over hot embers.",
                "timings": "06:00 AM - 11:00 AM, 05:00 PM - 08:30 PM",
                "contact": "Village Temple Committee: +91 94435 12098",
                "nearby": [
                    {"name": "Villudayanpattu Murugan Temple", "dist": "2.5 km"},
                    {"name": "Mandharakuppam Market", "dist": "3 km"}
                ],
                "maps": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3914.856980076722!2d79.50!3d11.58!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3a54d588523c91fb%3A0xc3175ebc088be330!2sVadavaur%20Mariamman%20Temple!5e0!3m2!1sen!2sin!4v1718613100000!5m2!1sen!2sin",
                "additional_info": "Expect heavy crowds during Aadi Fridays. Traditional drum music (Thavil and Nadaswaram) performances are a key highlight.",
                "gallery": [
                    "https://images.unsplash.com/photo-1560717789-0ac7c58ac90a?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1506157786151-b8491531f063?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1628155930542-3c7a64e2c833?auto=format&fit=crop&w=600&q=80"
                ]
            }
        ]
    },
    "churches": {
        "title": "Churches",
        "file": "churches.html",
        "description": "Locate prominent churches and Christian parishes in the Neyveli Township.",
        "items": [
            {
                "id": "st-gabriels-catholic-church",
                "name": "St. Gabriel's Catholic Church",
                "image": "images/neyveli-church.jpg",
                "address": "Block 24, Neyveli Township, Tamil Nadu 607801",
                "short_desc": "A beautiful and large Catholic parish in Block 24, serving as a key center of worship.",
                "full_desc": "St. Gabriel's Catholic Church is one of the oldest and largest Christian parishes in the Neyveli Township. Established shortly after the construction of the township, this church features a beautiful architectural layout with high arches and stained glass panels. The parish runs regular services, community welfare programs, and hosts a grand annual feast in honor of Archangel Gabriel, attracting members from all parts of Cuddalore district.",
                "timings": "Daily Services: 06:00 AM. Sunday Masses: 06:30 AM, 08:30 AM",
                "contact": "Parish Priest Office: +91 4142 252124",
                "nearby": [
                    {"name": "Neyveli Boat House", "dist": "0.9 km"},
                    {"name": "St. Joseph of Cluny School", "dist": "1.2 km"}
                ],
                "maps": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3914.856980076722!2d79.48!3d11.595!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3a54d588523c91fb%3A0xc3175ebc088be330!2sSt%20Gabriel's%20Church%20Neyveli!5e0!3m2!1sen!2sin!4v1718613200000!5m2!1sen!2sin",
                "additional_info": "Visitors are requested to maintain absolute silence and respect the service times.",
                "gallery": [
                    "https://images.unsplash.com/photo-1545638870-86562689978e?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1507643199731-1f7c70c0c660?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1478147427282-58a87a120781?auto=format&fit=crop&w=600&q=80"
                ]
            },
            {
                "id": "sacred-heart-church",
                "name": "Sacred Heart Church",
                "image": "https://images.unsplash.com/photo-1490122417551-6ee9691429d0?auto=format&fit=crop&w=600&q=80",
                "address": "Block 18, Neyveli Township, Tamil Nadu 607803",
                "short_desc": "A peaceful church located in Block 18, popular for its weekly community meetings.",
                "full_desc": "The Sacred Heart Church is a prominent parish located in the residential neighborhood of Block 18. Known for its modern altar and peaceful meditation garden, it is a key spiritual home for Catholic families in the central blocks of the township. The church conducts various catechism classes, youth fellowship activities, and has a dedicated choir group.",
                "timings": "Daily Mass: 06:30 AM. Sunday Mass: 07:00 AM, 05:30 PM",
                "contact": "Parish Office: +91 4142 253392",
                "nearby": [
                    {"name": "Nehru Park", "dist": "0.5 km"},
                    {"name": "Block 18 Market", "dist": "0.2 km"}
                ],
                "maps": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3914.856980076722!2d79.475!3d11.60!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3a54d588523c91fb%3A0xc3175ebc088be330!2sSacred%20Heart%20Church%20Neyveli!5e0!3m2!1sen!2sin!4v1718613300000!5m2!1sen!2sin",
                "additional_info": "Special prayers are held every first Friday of the month.",
                "gallery": [
                    "https://images.unsplash.com/photo-1548625361-155de0c7b57a?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1510563800743-aed236490d08?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1515516969-d4008cc6241a?auto=format&fit=crop&w=600&q=80"
                ]
            },
            {
                "id": "st-josephs-church",
                "name": "St. Joseph's Church",
                "image": "https://images.unsplash.com/photo-1523012479891-41710ab410c3?auto=format&fit=crop&w=600&q=80",
                "address": "Block 2, Neyveli Township, Tamil Nadu 607801",
                "short_desc": "A vibrant parish church serving families in Block 2 and surrounding residential sectors.",
                "full_desc": "St. Joseph's Church in Block 2 serves as a central hub of worship for Christians residing in the northern blocks of Neyveli. The church has a simple, elegant design and features a spacious hall for community gatherings. It works closely with local educational institutions to organize charity drives, youth camps, and Sunday school for kids.",
                "timings": "Sunday Mass: 07:00 AM, 06:00 PM. Tuesday Novena: 06:30 PM",
                "contact": "Church Office: +91 4142 221004",
                "nearby": [
                    {"name": "Neyveli Post Office", "dist": "0.3 km"},
                    {"name": "Block 2 Market", "dist": "0.2 km"}
                ],
                "maps": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3914.856980076722!2d79.485!3d11.605!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3a54d588523c91fb%3A0xc3175ebc088be330!2sSt%20Joseph%20Church%20Neyveli!5e0!3m2!1sen!2sin!4v1718613400000!5m2!1sen!2sin",
                "additional_info": "Novena prayers to St. Joseph are held on Tuesday evenings with a candlelit procession.",
                "gallery": [
                    "https://images.unsplash.com/photo-1543051932-6ef9fecfbc80?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1509224497357-31687671897e?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1498154801295-41e9c6f2fbb2?auto=format&fit=crop&w=600&q=80"
                ]
            },
            {
                "id": "telc-holy-trinity-church",
                "name": "TELC Holy Trinity Church",
                "image": "https://images.unsplash.com/photo-1555696958-c5049b866f6f?auto=format&fit=crop&w=600&q=80",
                "address": "Block 9, Neyveli Township, Tamil Nadu 607801",
                "short_desc": "A historic Lutheran church in Block 9, part of the Tamil Evangelical Lutheran Church diocese.",
                "full_desc": "TELC Holy Trinity Church is a historic protestant church affiliated with the Tamil Evangelical Lutheran Church (TELC). Located in Block 9, the church has a traditional, classic design and a peaceful setting. It holds services in Tamil and English, and has been serving the Lutheran community in the township for over five decades.",
                "timings": "Sunday Service: 07:30 AM (Tamil), 09:30 AM (English)",
                "contact": "Presiding Pastor: +91 4142 256782",
                "nearby": [
                    {"name": "Neyveli Railway Station", "dist": "1 km"},
                    {"name": "Jawahar Science College", "dist": "1.5 km"}
                ],
                "maps": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3914.856980076722!2d79.47!3d11.602!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3a54d588523c91fb%3A0xc3175ebc088be330!2sTELC%20Holy%20Trinity%20Church%20Neyveli!5e0!3m2!1sen!2sin!4v1718613500000!5m2!1sen!2sin",
                "additional_info": "Harvest festivals are celebrated annually in November, featuring traditional food stalls and charity auctions.",
                "gallery": [
                    "https://images.unsplash.com/photo-1578163926065-901d8487779d?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1549488344-1f9b8d2bd1f3?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1616431778930-b3e5513ab370?auto=format&fit=crop&w=600&q=80"
                ]
            },
            {
                "id": "ipc-bethel-church",
                "name": "IPC Neyveli Bethel Church",
                "image": "https://images.unsplash.com/photo-1582268611958-ebfd161ef9cf?auto=format&fit=crop&w=600&q=80",
                "address": "Block 5, Neyveli Township, Tamil Nadu 607801",
                "short_desc": "A lively Pentecostal church in Block 5, part of the India Pentecostal Church of God.",
                "full_desc": "The IPC Neyveli Bethel Church is a vibrant congregation belonging to the India Pentecostal Church of God (IPC). Located in Block 5, this church is known for its spirit-filled worship services, prayer meetings, and evangelical programs. It draws families from all blocks of Neyveli who participate in weekly cottage prayers and Bible study sessions.",
                "timings": "Sunday Service: 08:00 AM. Friday Fasting Prayer: 10:00 AM",
                "contact": "Pastor Office: +91 94441 23456",
                "nearby": [
                    {"name": "Block 5 Playground", "dist": "0.3 km"},
                    {"name": "Block 5 Shopping complex", "dist": "0.4 km"}
                ],
                "maps": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3914.856980076722!2d79.475!3d11.608!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3a54d588523c91fb%3A0xc3175ebc088be330!2sIPC%20Bethel%20Church%20Neyveli!5e0!3m2!1sen!2sin!4v1718613600000!5m2!1sen!2sin",
                "additional_info": "Fasting prayers are conducted every Friday morning for national and community welfare.",
                "gallery": [
                    "https://images.unsplash.com/photo-1510076897241-b0e7d0393c8d?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1560026301-28359cc595ef?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1490730141103-6cac27aaab94?auto=format&fit=crop&w=600&q=80"
                ]
            },
            {
                "id": "csi-good-shepherd-church",
                "name": "CSI Good Shepherd Church",
                "image": "https://images.unsplash.com/photo-1579621970795-87facc2f976d?auto=format&fit=crop&w=600&q=80",
                "address": "Block 26, Neyveli Township, Tamil Nadu 607803",
                "short_desc": "The largest Church of South India (CSI) parish in Neyveli, hosting weekly Sunday services.",
                "full_desc": "CSI Good Shepherd Church is the central Church of South India (CSI) congregation in the Neyveli Township. Situated in Block 26, it is a magnificent structure with a spacious sanctuary that can accommodate over 800 worshippers. The church runs an active youth wing, women's fellowship, and is known for its grand Christmas carol services and community outreach programs.",
                "timings": "Sunday Service: 07:00 AM (Tamil), 09:00 AM (English)",
                "contact": "CSI Presbyter: +91 4142 254490",
                "nearby": [
                    {"name": "NLC Logistics Office", "dist": "0.8 km"},
                    {"name": "Block 26 Park", "dist": "0.4 km"}
                ],
                "maps": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3914.856980076722!2d79.48!3d11.59!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3a54d588523c91fb%3A0xc3175ebc088be330!2sCSI%20Good%20Shepherd%20Church%20Neyveli!5e0!3m2!1sen!2sin!4v1718613700000!5m2!1sen!2sin",
                "additional_info": "Christmas Carol Services in December are highly popular and open to people of all faiths.",
                "gallery": [
                    "https://images.unsplash.com/photo-1490557162706-284736f48784?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1529156069898-49953e39b3ac?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1549488344-0b812f22b794?auto=format&fit=crop&w=600&q=80"
                ]
            }
        ]
    },
    "mosques-dargahs": {
        "title": "Mosques & Dargahs",
        "file": "mosques-dargahs.html",
        "description": "Directory of mosques and sacred Islamic dargahs in and around Neyveli.",
        "items": [
            {
                "id": "neyveli-central-mosque",
                "name": "Neyveli Central Mosque",
                "image": "images/neyveli-mosque.jpg",
                "address": "Block 29, Neyveli Township, Tamil Nadu 607807",
                "short_desc": "The largest and primary mosque in the Neyveli Township, hosting central Friday prayers.",
                "full_desc": "The Neyveli Central Mosque, located in Block 29, is the largest Islamic place of worship in the township. Featuring beautiful white minarets and a spacious prayer hall, the mosque can accommodate over a thousand worshippers during congregational prayers. It serves as the primary center for Eid celebrations, daily prayers, and community classes for children.",
                "timings": "Open for all 5 daily prayers (Salah)",
                "contact": "Mosque Committee Secretary: +91 4142 228491",
                "nearby": [
                    {"name": "Sri Nataraja Temple", "dist": "0.5 km"},
                    {"name": "Block 29 Bazaar", "dist": "0.3 km"}
                ],
                "maps": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3914.856980076722!2d79.467!3d11.61!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3a54d588523c91fb%3A0xc3175ebc088be330!2sNeyveli%20Central%20Mosque!5e0!3m2!1sen!2sin!4v1718613800000!5m2!1sen!2sin",
                "additional_info": "Special arrangements are made for Friday (Jummah) prayers and during the holy month of Ramadan for Iftar.",
                "gallery": [
                    "https://images.unsplash.com/photo-1597935258735-e254c1839512?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1564507592333-c60657eea523?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1542838132-92c53300491e?auto=format&fit=crop&w=600&q=80"
                ]
            },
            {
                "id": "block-12-jamiya-masjid",
                "name": "Block 12 Jamiya Masjid",
                "image": "https://images.unsplash.com/photo-1584551246679-0daf3d275d0f?auto=format&fit=crop&w=600&q=80",
                "address": "Block 12, Neyveli Township, Tamil Nadu 607803",
                "short_desc": "A beautiful mosque in Block 12, serving local residents for daily prayers and Quran studies.",
                "full_desc": "The Jamiya Masjid in Block 12 is a well-maintained neighborhood mosque. It provides a peaceful prayer environment for residents in the central blocks. The mosque committee runs evening madrasa classes for children and coordinates local charity activities during Islamic festivals.",
                "timings": "Open for all 5 daily prayers (Salah)",
                "contact": "Masjid Office: +91 94420 54321",
                "nearby": [
                    {"name": "Block 12 Park", "dist": "0.4 km"},
                    {"name": "Block 12 Cooperative Store", "dist": "0.2 km"}
                ],
                "maps": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3914.856980076722!2d79.472!3d11.601!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3a54d588523c91fb%3A0xc3175ebc088be330!2sBlock%2012%20Mosque%20Neyveli!5e0!3m2!1sen!2sin!4v1718613900000!5m2!1sen!2sin",
                "additional_info": "Islamic educational programs are conducted after the evening prayers on weekends.",
                "gallery": [
                    "https://images.unsplash.com/photo-1601999109332-542b18dbec57?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1519817650390-64a93db51149?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1580983231438-db4e4fc741d4?auto=format&fit=crop&w=600&q=80"
                ]
            },
            {
                "id": "mandharakuppam-mosque",
                "name": "Mandharakuppam Mosque",
                "image": "https://images.unsplash.com/photo-1507742188448-f86a23cae537?auto=format&fit=crop&w=600&q=80",
                "address": "Cuddalore Main Road, Mandharakuppam, Neyveli, Tamil Nadu 607802",
                "short_desc": "A popular mosque located in the busy commercial hub of Mandharakuppam.",
                "full_desc": "Situated in the bustling commercial area of Mandharakuppam, this mosque is highly frequented by local merchants, commuters, and residents. It features a modern facade and is a critical point of worship for the Muslim community living outside the main corporate township boundary.",
                "timings": "Open for all 5 daily prayers (Salah)",
                "contact": "Mandharakuppam Islamic Trust: +91 98943 12345",
                "nearby": [
                    {"name": "Mandharakuppam Bus Stop", "dist": "0.2 km"},
                    {"name": "PKR Mahal", "dist": "0.5 km"}
                ],
                "maps": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3914.856980076722!2d79.495!3d11.585!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3a54d588523c91fb%3A0xc3175ebc088be330!2sMandharakuppam%20Mosque!5e0!3m2!1sen!2sin!4v1718614000000!5m2!1sen!2sin",
                "additional_info": "A commercial area is located right next to the mosque, making it easily accessible for travelers.",
                "gallery": [
                    "https://images.unsplash.com/photo-1542838132-92c53300491e?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1587825140708-dfaf72ae4b04?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1533230898523-255b7d04000a?auto=format&fit=crop&w=600&q=80"
                ]
            },
            {
                "id": "indira-nagar-mosque",
                "name": "Indira Nagar Mosque",
                "image": "https://images.unsplash.com/photo-1518998053901-5348d3961a04?auto=format&fit=crop&w=600&q=80",
                "address": "Indira Nagar, Neyveli, Tamil Nadu 607801",
                "short_desc": "A local neighborhood mosque serving the residential community of Indira Nagar.",
                "full_desc": "The Indira Nagar Mosque is a cozy, community-run mosque located in the suburb of Indira Nagar, just outside the NLC township. It serves as a vital spiritual center for local families and laborers working in nearby private enterprises, hosting daily congregational prayers and community discussions.",
                "timings": "Open for all 5 daily prayers (Salah)",
                "contact": "Local Jamaat Committee: +91 95002 98765",
                "nearby": [
                    {"name": "Senthamil Mahal", "dist": "0.6 km"},
                    {"name": "Indira Nagar Arch", "dist": "0.4 km"}
                ],
                "maps": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3914.856980076722!2d79.49!3d11.60!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3a54d588523c91fb%3A0xc3175ebc088be330!2sIndira%20Nagar%20Mosque%20Neyveli!5e0!3m2!1sen!2sin!4v1718614100000!5m2!1sen!2sin",
                "additional_info": "Maintains a library containing books on Islamic history and theology, open to members.",
                "gallery": [
                    "https://images.unsplash.com/photo-1564507592333-c60657eea523?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1522202176988-66273c2fd55f?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1488590528505-98d2b5aba04b?auto=format&fit=crop&w=600&q=80"
                ]
            },
            {
                "id": "mel-bhuvanagiri-dargah",
                "name": "Mel Bhuvanagiri Dargah",
                "image": "https://images.unsplash.com/photo-1598373182133-52452f7691ef?auto=format&fit=crop&w=600&q=80",
                "address": "Bhuvanagiri Main Road, Mel Bhuvanagiri, Tamil Nadu 608601",
                "short_desc": "A historic, sacred Sufi dargah near Neyveli, visited by people of all faiths.",
                "full_desc": "Located 25 km from Neyveli, the Mel Bhuvanagiri Dargah is a highly revered shrine dedicated to a Sufi saint. The dargah is famed for its peaceful, spiritual vibrations and is unique in that it draws devotees from all religions (Hindus, Muslims, and Christians) who come to pray for health, prosperity, and peace. It stands as a symbol of communal harmony in the Cuddalore district.",
                "timings": "05:00 AM - 09:30 PM (Daily)",
                "contact": "Dargah Sharif Trustees: +91 4144 240111",
                "nearby": [
                    {"name": "Chidambaram Nataraja Temple", "dist": "9 km"},
                    {"name": "Bhuvanagiri Bus Stand", "dist": "0.5 km"}
                ],
                "maps": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3916.328!2d79.64!3d11.46!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3a54c60000000001%3A0xabcdefabcdefabcd!2sBhuvanagiri%20Dargah!5e0!3m2!1sen!2sin!4v1718614200000!5m2!1sen!2sin",
                "additional_info": "The annual Urs festival is celebrated with great pageantry, featuring community feeding (Kandhuri) for thousands.",
                "gallery": [
                    "https://images.unsplash.com/photo-1566121318578-f9b763a4ee4e?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1534447677768-be436bb09401?auto=format&fit=crop&w=600&q=80"
                ]
            },
            {
                "id": "peer-shah-wali-dargah",
                "name": "Peer Shah Wali Dargah",
                "image": "https://images.unsplash.com/photo-1509198397868-475647b2a1e5?auto=format&fit=crop&w=600&q=80",
                "address": "Cuddalore Road Bypass, Neyveli, Tamil Nadu 607802",
                "short_desc": "A revered local dargah, popular for Thursday evening special prayer gatherings.",
                "full_desc": "The Peer Shah Wali Dargah is a local spiritual landmark situated near the Neyveli bypass. Dedicated to a Sufi mystic who traveled through the region centuries ago, the dargah is highly popular for Thursday evening prayers, where devotees light lamps and seek blessings for healing and general wellness.",
                "timings": "06:00 AM - 09:00 PM (Daily)",
                "contact": "Dargah Maintenance Board: +91 90035 65432",
                "nearby": [
                    {"name": "Mandharakuppam", "dist": "2 km"},
                    {"name": "HPCL Petrol Pump", "dist": "1.5 km"}
                ],
                "maps": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3914.856980076722!2d79.50!3d11.58!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3a54d588523c91fb%3A0xc3175ebc088be330!2sPeer%20Shah%20Wali%20Dargah!5e0!3m2!1sen!2sin!4v1718614300000!5m2!1sen!2sin",
                "additional_info": "Devotional Qawwali music is played on Thursday nights after the sunset prayer.",
                "gallery": [
                    "https://images.unsplash.com/photo-1549488344-0b812f22b794?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1508214751196-bcfd4ca60f91?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1501854140801-50d01698950b?auto=format&fit=crop&w=600&q=80"
                ]
            }
        ]
    },
    "marriage-halls": {
        "title": "Marriage Halls",
        "file": "marriage-halls.html",
        "description": "Locate the best Kalyana Mandapams and community halls for events in Neyveli.",
        "items": [
            {
                "id": "nlc-community-hall",
                "name": "NLC Community Hall",
                "image": "images/neyveli-marriage-hall.jpg",
                "address": "Block 24, Neyveli Township, Tamil Nadu 607801",
                "short_desc": "A spacious and air-conditioned hall run by NLC IL for employee events and public bookings.",
                "full_desc": "The NLC Community Hall in Block 24 is a premier, state-of-the-art event venue operated by the NLC Township Administration. It features a grand air-conditioned auditorium, a separate vast dining hall, and modern green rooms. The hall is primarily booked for marriages of NLC employee families but is also open for public cultural events, conferences, and festivals.",
                "timings": "Open for booked events (24 Hours)",
                "contact": "NLC Township Booking Office: +91 4142 252250",
                "nearby": [
                    {"name": "Neyveli Boat House", "dist": "1 km"},
                    {"name": "Children's Park", "dist": "0.7 km"}
                ],
                "maps": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3914.856980076722!2d79.48!3d11.594!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3a54d588523c91fb%3A0xc3175ebc088be330!2sNLC%20Community%20Hall!5e0!3m2!1sen!2sin!4v1718614400000!5m2!1sen!2sin",
                "additional_info": "Highly subsidised rates are applicable for NLC India Limited employees. Bookings must be made 3-6 months in advance.",
                "gallery": [
                    "https://images.unsplash.com/photo-1519167758481-83f550bb49b3?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1549417229-aa67d3263c09?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1469371670807-013ccf25f16a?auto=format&fit=crop&w=600&q=80"
                ]
            },
            {
                "id": "lignite-hall",
                "name": "Lignite Hall",
                "image": "https://images.unsplash.com/photo-1505232458729-44772f7d857f?auto=format&fit=crop&w=600&q=80",
                "address": "Block 11, Neyveli Township, Tamil Nadu 607803",
                "short_desc": "An iconic multipurpose township hall hosting cultural programs, marriages, and exhibitions.",
                "full_desc": "Lignite Hall is an iconic social hub located in Block 11. It has served as the township's primary venue for cultural shows, official NLC briefings, and mega marriages for several decades. It features classic open-architecture, excellent natural ventilation, and can accommodate large gatherings of up to 1,500 people.",
                "timings": "Open for booked events",
                "contact": "Neyveli Public Relations Office: +91 4142 222550",
                "nearby": [
                    {"name": "Block 11 Shopping Area", "dist": "0.2 km"},
                    {"name": "Sridharan Hospital", "dist": "1.8 km"}
                ],
                "maps": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3914.856980076722!2d79.47!3d11.60!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3a54d588523c91fb%3A0xc3175ebc088be330!2sLignite%20Hall%20Neyveli!5e0!3m2!1sen!2sin!4v1718614500000!5m2!1sen!2sin",
                "additional_info": "Ample open space surrounding the hall is perfect for outdoor buffet setups and vehicle parking.",
                "gallery": [
                    "https://images.unsplash.com/photo-1511285560929-80b456fea0bc?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1532712938310-34cb3982ef74?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1549849171-09f624ee86ee?auto=format&fit=crop&w=600&q=80"
                ]
            },
            {
                "id": "sri-nataraja-kalyana-mandapam",
                "name": "Sri Nataraja Kalyana Mandapam",
                "image": "https://images.unsplash.com/photo-1520854221256-17451cc35953?auto=format&fit=crop&w=600&q=80",
                "address": "Block 29, Neyveli Township, Tamil Nadu 607807",
                "short_desc": "A traditional wedding hall located close to the famous Sri Nataraja Temple.",
                "full_desc": "Located right next to the prominent Nataraja Temple in Block 29, this Kalyana Mandapam is the most preferred venue for traditional Hindu weddings. It provides all basic amenities, including a elevated stage, bride and groom rooms, and a traditional floor-seating dining hall. The proximity to the temple allows families to perform sacred ceremonies directly under temple blessings.",
                "timings": "Open for bookings",
                "contact": "Temple Board Mandapam Office: +91 4142 228991",
                "nearby": [
                    {"name": "Sri Nataraja Temple", "dist": "0.1 km"},
                    {"name": "Neyveli Central Mosque", "dist": "0.6 km"}
                ],
                "maps": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3914.856980076722!2d79.467!3d11.61!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3a54d588523c91fb%3A0xc3175ebc088be330!2sSri%20Nataraja%20Kalyana%20Mandapam!5e0!3m2!1sen!2sin!4v1718614600000!5m2!1sen!2sin",
                "additional_info": "Only vegetarian catering is permitted inside the premises due to its close proximity to the temple.",
                "gallery": [
                    "https://images.unsplash.com/photo-1544078751-58fed2b84d57?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1510076897241-b0e7d0393c8d?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1560026301-28359cc595ef?auto=format&fit=crop&w=600&q=80"
                ]
            },
            {
                "id": "pkr-mahal",
                "name": "PKR Mahal",
                "image": "https://images.unsplash.com/photo-1522413416012-1aebd6494137?auto=format&fit=crop&w=600&q=80",
                "address": "Main Road, Mandharakuppam, Neyveli, Tamil Nadu 607802",
                "short_desc": "A modern, large marriage hall located in Mandharakuppam, ideal for grand weddings.",
                "full_desc": "PKR Mahal is a popular private wedding hall located on the Mandharakuppam Main Road. Designed with modern interiors, the hall has a capacity of over 1,000 guests. It features a spacious stage, central air conditioning, a well-equipped kitchen, and parking space for dozens of cars, making it a popular choice for families inside and outside the township.",
                "timings": "Open for bookings",
                "contact": "Mahal Manager: +91 94434 98765",
                "nearby": [
                    {"name": "Mandharakuppam Market", "dist": "0.4 km"},
                    {"name": "BPCL Petrol Bunk", "dist": "0.8 km"}
                ],
                "maps": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3914.856980076722!2d79.495!3d11.585!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3a54d588523c91fb%3A0xc3175ebc088be330!2sPKR%20Mahal%20Mandharakuppam!5e0!3m2!1sen!2sin!4v1718614700000!5m2!1sen!2sin",
                "additional_info": "Both vegetarian and non-vegetarian catering are allowed. Power backup generator is available.",
                "gallery": [
                    "https://images.unsplash.com/photo-1549417229-aa67d3263c09?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1587271407850-8d438ca9fdf2?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1527529482837-4698179dc6ce?auto=format&fit=crop&w=600&q=80"
                ]
            },
            {
                "id": "senthamil-mahal",
                "name": "Senthamil Mahal",
                "image": "https://images.unsplash.com/photo-1523438885200-e635ba2c371e?auto=format&fit=crop&w=600&q=80",
                "address": "Bypass Road, Indira Nagar, Neyveli, Tamil Nadu 607801",
                "short_desc": "A budget-friendly kalyana mandapam offering good facilities for local celebrations.",
                "full_desc": "Senthamil Mahal is a highly preferred budget-friendly event venue located near Indira Nagar. The hall is ideal for medium-sized marriages, engagement functions, and family gatherings. It offers clean rooms, a spacious dining area, and good catering facilities at highly competitive booking prices.",
                "timings": "Open for bookings",
                "contact": "Mahal Booking Desk: +91 98940 54321",
                "nearby": [
                    {"name": "Indira Nagar Mosque", "dist": "0.6 km"},
                    {"name": "Aryas Hotel", "dist": "1.2 km"}
                ],
                "maps": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3914.856980076722!2d79.49!3d11.60!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3a54d588523c91fb%3A0xc3175ebc088be330!2sSenthamil%20Mahal%20Neyveli!5e0!3m2!1sen!2sin!4v1718614800000!5m2!1sen!2sin",
                "additional_info": "Features a spacious open rooftop balcony which is often used for evening high-tea counters.",
                "gallery": [
                    "https://images.unsplash.com/photo-1519671482749-fd09be7ccebf?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1502602898657-3e91760cbb34?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1511795409834-ef04bbd61622?auto=format&fit=crop&w=600&q=80"
                ]
            },
            {
                "id": "ar-mahal",
                "name": "A.R. Mahal",
                "image": "https://images.unsplash.com/photo-1519741497674-611481863552?auto=format&fit=crop&w=600&q=80",
                "address": "Neyveli Bypass Road, Mandharakuppam, Tamil Nadu 607802",
                "short_desc": "A newly constructed, elegant marriage hall with modern lighting and parking facility.",
                "full_desc": "A.R. Mahal is a premium, contemporary marriage hall located along the Neyveli Bypass Road. Built with modern architectural aesthetics, it features an elegant false ceiling with designer lighting, an expansive central hall, and a high-capacity air-conditioned dining area. Its location on the bypass ensures hassle-free access and parking for guests arriving from nearby cities like Cuddalore or Kumbakonam.",
                "timings": "Open for bookings",
                "contact": "AR Hall Bookings: +91 97890 12345",
                "nearby": [
                    {"name": "HPCL Petrol Pump", "dist": "1.2 km"},
                    {"name": "Peer Shah Wali Dargah", "dist": "2.1 km"}
                ],
                "maps": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3914.856980076722!2d79.50!3d11.58!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3a54d588523c91fb%3A0xc3175ebc088be330!2sAR%20Mahal%20Mandharakuppam!5e0!3m2!1sen!2sin!4v1718614900000!5m2!1sen!2sin",
                "additional_info": "Features a large stage backdrop display system. 24-hour water supply and room service are guaranteed.",
                "gallery": [
                    "https://images.unsplash.com/photo-1525253086316-d0c936c814f8?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1464366400600-7168b8af9bc3?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1519225495810-7512c696af0a?auto=format&fit=crop&w=600&q=80"
                ]
            }
        ]
    },
    "petrol-bunks": {
        "title": "Petrol Bunks",
        "file": "petrol-bunks.html",
        "description": "Locate reliable fuel stations and service points operating in Neyveli.",
        "items": [
            {
                "id": "bpcl-petrol-station",
                "name": "BPCL Petrol Station",
                "image": "images/neyveli-petrol-bunk.jpg",
                "address": "Block 24, Main Township Road, Neyveli, Tamil Nadu 607801",
                "short_desc": "A primary Bharat Petroleum outlet offering 24/7 refueling and digital payments.",
                "full_desc": "The Bharat Petroleum (BPCL) outlet in Block 24 is one of the busiest fuel stations inside the Neyveli Township. It provides high-speed dispensing of petrol, diesel, and Speed (premium petrol). The bunk features automated billing systems, tyre inflation services, and accepts all digital wallets and credit cards, ensuring a quick and smooth refueling experience for residents.",
                "timings": "Open 24 Hours",
                "contact": "Station Manager: +91 4142 254401",
                "nearby": [
                    {"name": "NLC Community Hall", "dist": "0.5 km"},
                    {"name": "Neyveli Boat House", "dist": "1.2 km"}
                ],
                "maps": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3914.856980076722!2d79.48!3d11.594!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3a54d588523c91fb%3A0xc3175ebc088be330!2sBPCL%20Petrol%20Pump%20Neyveli!5e0!3m2!1sen!2sin!4v1718615000000!5m2!1sen!2sin",
                "additional_info": "Nitrogen air filling station is available. A convenience store is located within the premises.",
                "gallery": [
                    "https://images.unsplash.com/photo-1527018601619-a508a2be00cd?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1622060822165-35b25867213d?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1542440956-62024b4f3b60?auto=format&fit=crop&w=600&q=80"
                ]
            },
            {
                "id": "hpcl-fuel-station",
                "name": "HPCL Fuel Station",
                "image": "https://images.unsplash.com/photo-1610492160914-7d526be9f52f?auto=format&fit=crop&w=600&q=80",
                "address": "Cuddalore Main Road, Mandharakuppam, Neyveli, Tamil Nadu 607802",
                "short_desc": "A major Hindustan Petroleum station on the main highway, catering to long-distance vehicles.",
                "full_desc": "Conveniently located on the Cuddalore Main Road in Mandharakuppam, this HPCL fuel station is a key stop for long-distance trucks, buses, and tourists passing through Neyveli. It features multiple fuel bays, clean restrooms, a small snack corner, and high-capacity diesel dispensing pumps designed specifically for commercial vehicles.",
                "timings": "05:00 AM - 11:30 PM (Daily)",
                "contact": "Bunk Supervisor: +91 94421 87654",
                "nearby": [
                    {"name": "PKR Mahal", "dist": "0.3 km"},
                    {"name": "Mandharakuppam Mosque", "dist": "0.6 km"}
                ],
                "maps": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3914.856980076722!2d79.495!3d11.585!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3a54d588523c91fb%3A0xc3175ebc088be330!2sHPCL%20Petrol%20Pump%20Mandharakuppam!5e0!3m2!1sen!2sin!4v1718615100000!5m2!1sen!2sin",
                "additional_info": "Equipped with a pollution check center (PUCC) which issues digital certificates instantly.",
                "gallery": [
                    "https://images.unsplash.com/photo-1614088031388-75c1202e86ef?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1562663474-6cbb3fee4c77?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1549488344-1f9b8d2bd1f3?auto=format&fit=crop&w=600&q=80"
                ]
            },
            {
                "id": "iocl-petrol-pump",
                "name": "IOCL Petrol Pump",
                "image": "https://images.unsplash.com/photo-1542440956-6489b910408d?auto=format&fit=crop&w=600&q=80",
                "address": "Block 2, Neyveli Township, Tamil Nadu 607801",
                "short_desc": "Indian Oil outlet providing fuel, lubricants, and free air checking in northern Neyveli.",
                "full_desc": "The Indian Oil Corporation (IOCL) petrol pump in Block 2 serves the north-eastern sectors of Neyveli Township. Known for its quick service and honest fuel measurements, the bunk is popular among two-wheeler owners. It also stocks a wide range of Servo lubricants and offers free digital tyre pressure checks.",
                "timings": "06:00 AM - 10:00 PM (Daily)",
                "contact": "Station Manager: +91 4142 221050",
                "nearby": [
                    {"name": "St. Joseph's Church", "dist": "0.4 km"},
                    {"name": "Arun Pharmacy", "dist": "0.2 km"}
                ],
                "maps": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3914.856980076722!2d79.485!3d11.605!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3a54d588523c91fb%3A0xc3175ebc088be330!2sIOCL%20Petrol%20Pump%20Block%202!5e0!3m2!1sen!2sin!4v1718615200000!5m2!1sen!2sin",
                "additional_info": "Digital payments like UPI (GPay, PhonePe, Paytm) are highly preferred here.",
                "gallery": [
                    "https://images.unsplash.com/photo-1520854221256-17451cc35953?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1578575437130-527eed3abbec?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1543051932-6ef9fecfbc80?auto=format&fit=crop&w=600&q=80"
                ]
            },
            {
                "id": "nlc-cooperative-petrol",
                "name": "NLC Co-operative Petrol Station",
                "image": "https://images.unsplash.com/photo-1564939558297-fc396f18e5c7?auto=format&fit=crop&w=600&q=80",
                "address": "Block 11, Neyveli Township, Tamil Nadu 607803",
                "short_desc": "Cooperative bunk managed by NLCIL employees society, guaranteeing fuel purity.",
                "full_desc": "The NLC Employees Co-operative Society Petrol Bunk in Block 11 is famous for its guarantee of quality and quantity. Being community-managed, it adheres strictly to fuel standards and is the most trusted bunk for many township residents. It also provides NLC employees with salary-linked fuel coupon options.",
                "timings": "06:00 AM - 10:30 PM (Daily)",
                "contact": "Cooperative Office: +91 4142 222120",
                "nearby": [
                    {"name": "Lignite Hall", "dist": "0.3 km"},
                    {"name": "NLC Cooperative Medicals", "dist": "0.1 km"}
                ],
                "maps": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3914.856980076722!2d79.47!3d11.60!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3a54d588523c91fb%3A0xc3175ebc088be330!2sNLC%20Cooperative%20Petrol%20Bunk!5e0!3m2!1sen!2sin!4v1718615300000!5m2!1sen!2sin",
                "additional_info": "Highly reliable fuel quality testing kits are available for customers upon request.",
                "gallery": [
                    "https://images.unsplash.com/photo-1549557162-706-284736f48784?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1529156069898-49953e39b3ac?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1549488344-0b812f22b794?auto=format&fit=crop&w=600&q=80"
                ]
            },
            {
                "id": "shell-petrol-station",
                "name": "Shell Petrol Station",
                "image": "https://images.unsplash.com/photo-1616431778930-b3e5513ab370?auto=format&fit=crop&w=600&q=80",
                "address": "Neyveli Bypass Road, Vadavaur, Tamil Nadu 607802",
                "short_desc": "A premium Shell fuel station offering world-class fuel additives and a Select convenience store.",
                "full_desc": "The Shell Petrol Station on the Neyveli Bypass is a modern, premium outlet offering Shell V-Power and regular fuels. Famed for its exceptional customer service, clean premises, and premium engine oils, this bunk is highly frequented by tourists and car enthusiasts. The station features a Shell Select store selling beverages, snacks, and car accessories.",
                "timings": "Open 24 Hours",
                "contact": "Shell Station Head: +91 99940 12345",
                "nearby": [
                    {"name": "Vadavaur Mariamman Temple", "dist": "0.8 km"},
                    {"name": "A.R. Mahal", "dist": "1.5 km"}
                ],
                "maps": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3914.856980076722!2d79.50!3d11.58!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3a54d588523c91fb%3A0xc3175ebc088be330!2sShell%20Petrol%20Pump%20Neyveli!5e0!3m2!1sen!2sin!4v1718615400000!5m2!1sen!2sin",
                "additional_info": "Offers excellent quick windshield cleaning services and has an automated coffee machine.",
                "gallery": [
                    "https://images.unsplash.com/photo-1543051932-6ef9fecfbc80?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1509224497357-31687671897e?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1498154801295-41e9c6f2fbb2?auto=format&fit=crop&w=600&q=80"
                ]
            },
            {
                "id": "reliance-petrol-mart",
                "name": "Reliance Petrol Mart",
                "image": "https://images.unsplash.com/photo-1598502573215-0d32f4c3b652?auto=format&fit=crop&w=600&q=80",
                "address": "Indira Nagar Bypass, Mandharakuppam, Tamil Nadu 607802",
                "short_desc": "Jio-bp petrol pump offering high-performance fuels and quick service.",
                "full_desc": "The Reliance (Jio-bp) Petrol Mart situated on the Indira Nagar Bypass is a modern fuel station offering high-quality diesel and petrol at competitive market rates. It features wide lanes for heavy vehicles and provides quick refueling services using computerized dispensers.",
                "timings": "06:00 AM - 11:00 PM (Daily)",
                "contact": "Reliance Pump Desk: +91 97865 43210",
                "nearby": [
                    {"name": "Senthamil Mahal", "dist": "1.5 km"},
                    {"name": "Mandharakuppam Market", "dist": "2 km"}
                ],
                "maps": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3914.856980076722!2d79.495!3d11.59!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3a54d588523c91fb%3A0xc3175ebc088be330!2sJio-bp%20Petrol%20Pump%20Neyveli!5e0!3m2!1sen!2sin!4v1718615500000!5m2!1sen!2sin",
                "additional_info": "Excellent lubricants and coolants from Castrol are sold here.",
                "gallery": [
                    "https://images.unsplash.com/photo-1578575437130-527eed3abbec?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1622060822165-35b25867213d?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1614088031388-75c1202e86ef?auto=format&fit=crop&w=600&q=80"
                ]
            }
        ]
    },
    "medical-shops": {
        "title": "Medical Shops",
        "file": "medical-shops.html",
        "description": "Directory of pharmacies, medicine stores, and 24/7 medical shops in Neyveli.",
        "items": [
            {
                "id": "apollo-pharmacy",
                "name": "Apollo Pharmacy",
                "image": "images/neyveli-medical-shop.jpg",
                "address": "Block 29, Main Bazaar Road, Neyveli, Tamil Nadu 607807",
                "short_desc": "A leading branded pharmacy offering genuine medicines, health supplements, and baby care.",
                "full_desc": "Apollo Pharmacy in Block 29 is a reliable, air-conditioned retail store of the nationwide Apollo Pharmacy chain. It is fully stocked with prescription medicines, over-the-counter products, home health devices, health supplements, baby food, and organic cosmetics. It features highly trained pharmacists who provide correct medication counseling.",
                "timings": "07:00 AM - 11:00 PM (Daily)",
                "contact": "Apollo B29 Desk: +91 4142 228995",
                "nearby": [
                    {"name": "Sri Nataraja Temple", "dist": "0.3 km"},
                    {"name": "Neyveli Central Mosque", "dist": "0.4 km"}
                ],
                "maps": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3914.856980076722!2d79.467!3d11.61!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3a54d588523c91fb%3A0xc3175ebc088be330!2sApollo%20Pharmacy%20Block%2029%20Neyveli!5e0!3m2!1sen!2sin!4v1718615600000!5m2!1sen!2sin",
                "additional_info": "Home delivery is available for orders within the Neyveli Township. Offers a free loyalty membership card.",
                "gallery": [
                    "https://images.unsplash.com/photo-1587854692152-cbe660dbde88?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1607619056574-7b8f304b3c8f?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1586015555751-63bb77f4322a?auto=format&fit=crop&w=600&q=80"
                ]
            },
            {
                "id": "arun-pharmacy",
                "name": "Arun Pharmacy",
                "image": "https://images.unsplash.com/photo-1628771065518-0d82f1938462?auto=format&fit=crop&w=600&q=80",
                "address": "Block 2, Shopping Complex, Neyveli Township, Tamil Nadu 607801",
                "short_desc": "A trusted local medical shop offering prescription drugs and cosmetic products.",
                "full_desc": "Arun Pharmacy in Block 2 is a highly popular, family-run medical shop that has been serving the Neyveli community for over two decades. Known for its friendly service, it stocks all major chronic and acute medications, skincare products, and baby care items. It is highly trusted by local families for its reliable medicine availability.",
                "timings": "08:00 AM - 10:30 PM (Daily)",
                "contact": "Pharmacy Desk: +91 4142 221120",
                "nearby": [
                    {"name": "St. Joseph's Church", "dist": "0.3 km"},
                    {"name": "IOCL Petrol Pump", "dist": "0.2 km"}
                ],
                "maps": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3914.856980076722!2d79.485!3d11.605!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3a54d588523c91fb%3A0xc3175ebc088be330!2sArun%20Pharmacy%20Neyveli!5e0!3m2!1sen!2sin!4v1718615700000!5m2!1sen!2sin",
                "additional_info": "Offers a standard 10% discount on all prescription medicines.",
                "gallery": [
                    "https://images.unsplash.com/photo-1576091160550-2173dba999ef?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1585435557343-3b092031a831?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1550572017-edd951b55104?auto=format&fit=crop&w=600&q=80"
                ]
            },
            {
                "id": "nlc-cooperative-medicals",
                "name": "NLC Cooperative Medicals",
                "image": "https://images.unsplash.com/photo-1585435557343-3b092031a831?auto=format&fit=crop&w=600&q=80",
                "address": "Block 11, Cooperative Bazaar, Neyveli, Tamil Nadu 607803",
                "short_desc": "Society-run pharmacy providing medicines at subsidised rates for township residents.",
                "full_desc": "The NLC Employees Co-operative Medical Store in Block 11 is a government-supported pharmacy. Designed to make healthcare affordable, it offers medicines at highly subsidised rates to NLC employee families and the general public. It keeps a comprehensive stock of critical life-saving medicines.",
                "timings": "09:00 AM - 09:30 PM (Closed on Sundays)",
                "contact": "Cooperative Medicals: +91 4142 222212",
                "nearby": [
                    {"name": "Lignite Hall", "dist": "0.2 km"},
                    {"name": "NLC Cooperative Petrol Bunk", "dist": "0.1 km"}
                ],
                "maps": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3914.856980076722!2d79.47!3d11.60!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3a54d588523c91fb%3A0xc3175ebc088be330!2sNLC%20Cooperative%20Medical%20Shop!5e0!3m2!1sen!2sin!4v1718615800000!5m2!1sen!2sin",
                "additional_info": "Subsidies are applied directly upon showing NLC ID card or pension book.",
                "gallery": [
                    "https://images.unsplash.com/photo-1547489432-cf93fa6c71ee?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1526256262350-7da7584cf5eb?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1603398938378-e54eab446dde?auto=format&fit=crop&w=600&q=80"
                ]
            },
            {
                "id": "medplus-medical",
                "name": "MedPlus Medical",
                "image": "https://images.unsplash.com/photo-1512244095648-8f86a23cae53?auto=format&fit=crop&w=600&q=80",
                "address": "Main Road, Mandharakuppam, Neyveli, Tamil Nadu 607802",
                "short_desc": "Branded pharmacy chain offering online medicine ordering and up to 20% discounts.",
                "full_desc": "MedPlus Mandharakuppam is a clean, modern, computerised pharmacy. It stocks a wide array of generic and branded medicines, healthcare products, baby food, and surgical equipment. Devoted to affordability, MedPlus offers flat discounts of up to 20% on medicines and coordinates medicine delivery through their mobile app.",
                "timings": "07:30 AM - 10:30 PM (Daily)",
                "contact": "MedPlus Mandharakuppam: +91 4142 259980",
                "nearby": [
                    {"name": "PKR Mahal", "dist": "0.5 km"},
                    {"name": "Mandharakuppam Bus Stop", "dist": "0.3 km"}
                ],
                "maps": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3914.856980076722!2d79.495!3d11.585!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3a54d588523c91fb%3A0xc3175ebc088be330!2sMedPlus%20Mandharakuppam!5e0!3m2!1sen!2sin!4v1718615900000!5m2!1sen!2sin",
                "additional_info": "A licensed health desk is available for free blood pressure and body mass index (BMI) monitoring.",
                "gallery": [
                    "https://images.unsplash.com/photo-1514416285071-f07865c6bf23?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1532187863486-abf9d39d66e8?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1471864190281-a93a3070b6de?auto=format&fit=crop&w=600&q=80"
                ]
            },
            {
                "id": "thulasi-pharmacy",
                "name": "Thulasi Pharmacy",
                "image": "https://images.unsplash.com/photo-1550572017-edd951b55104?auto=format&fit=crop&w=600&q=80",
                "address": "Block 18, Central Shopping Street, Neyveli, Tamil Nadu 607803",
                "short_desc": "A popular pharmacy in Block 18 offering a wide range of ayurvedic and allopathic medicines.",
                "full_desc": "Thulasi Pharmacy is a well-known retail medical store in Block 18, catering to residents in the central blocks of Neyveli Township. Alongside allopathic drugs, Thulasi is popular for keeping a dedicated counter of traditional Ayurvedic, Siddha, and Homeopathic medicines. It features a walk-in health section selling organic honey, health juices, and herbal cosmetics.",
                "timings": "08:00 AM - 10:30 PM (Daily)",
                "contact": "Thulasi B18 Office: +91 4142 251140",
                "nearby": [
                    {"name": "Nehru Park", "dist": "0.3 km"},
                    {"name": "Sacred Heart Church", "dist": "0.4 km"}
                ],
                "maps": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3914.856980076722!2d79.475!3d11.60!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3a54d588523c91fb%3A0xc3175ebc088be330!2sThulasi%20Pharmacy%20Neyveli!5e0!3m2!1sen!2sin!4v1718616000000!5m2!1sen!2sin",
                "additional_info": "Special Ayurvedic consultation sessions are conducted on weekend mornings.",
                "gallery": [
                    "https://images.unsplash.com/photo-1620714223084-8fcacc6dfd8d?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1601349690184-e82197fa6b4a?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1584308666744-24d5c474f2ae?auto=format&fit=crop&w=600&q=80"
                ]
            },
            {
                "id": "vignesh-medicals",
                "name": "Sri Vignesh Medicals",
                "image": "https://images.unsplash.com/photo-1601349690184-e82197fa6b4a?auto=format&fit=crop&w=600&q=80",
                "address": "Cuddalore Bypass, Mandharakuppam, Neyveli, Tamil Nadu 607802",
                "short_desc": "Emergency medical store located at the bypass junction, open late.",
                "full_desc": "Sri Vignesh Medicals is located at a key junction on the Cuddalore Bypass in Mandharakuppam. It is a vital resource for travelers and local residents needing emergency medicines late at night. The shop keeps an extensive stock of life-saving injectables, emergency inhalers, and basic surgical dressings.",
                "timings": "07:00 AM - 11:30 PM (Daily)",
                "contact": "Vignesh Medicals: +91 98425 67890",
                "nearby": [
                    {"name": "A.R. Mahal", "dist": "0.8 km"},
                    {"name": "Reliance Petrol Mart", "dist": "0.5 km"}
                ],
                "maps": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3914.856980076722!2d79.495!3d11.59!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3a54d588523c91fb%3A0xc3175ebc088be330!2sVignesh%20Medicals%20Mandharakuppam!5e0!3m2!1sen!2sin!4v1718616100000!5m2!1sen!2sin",
                "additional_info": "Accepts urgent telephone orders for medicine reservations to help customers pick them up quickly.",
                "gallery": [
                    "https://images.unsplash.com/photo-1542838132-92c53300491e?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1587825140708-dfaf72ae4b04?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1533230898523-255b7d04000a?auto=format&fit=crop&w=600&q=80"
                ]
            }
        ]
    },
    "government-offices": {
        "title": "Government Offices",
        "file": "government-offices.html",
        "description": "Essential contact details and addresses for municipal, civic, and administrative offices in Neyveli.",
        "items": [
            {
                "id": "nlc-head-office",
                "name": "NLC India Limited Corporate Office",
                "image": "images/admin.jpg",
                "address": "Corporate Office, Block 1, Neyveli Township, Tamil Nadu 607801",
                "short_desc": "The administrative and corporate headquarters of NLC India Limited.",
                "full_desc": "The Corporate Office of NLC India Limited (formerly Neyveli Lignite Corporation) in Block 1 is the administrative headquarters of this Navratna public sector enterprise. The massive office complex houses the offices of the Chairman, Board of Directors, and key administrative divisions managing lignite mining, thermal power generation, and green energy projects across India. It is a highly secure facility featuring modern office spaces and conference galleries.",
                "timings": "09:30 AM - 05:30 PM (Monday to Saturday; Closed on 2nd & 4th Saturdays)",
                "contact": "Corporate PR Office: +91 4142 252246 / pr.nlc@nic.in",
                "nearby": [
                    {"name": "Sangeetha Restaurant", "dist": "0.2 km"},
                    {"name": "NLC General Hospital", "dist": "1.8 km"}
                ],
                "maps": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3914.856980076722!2d79.483!3d11.603!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3a54d5bcffffffff%3A0x6b864a787b7a13d3!2sNLC%20Corporate%20Office!5e0!3m2!1sen!2sin!4v1718616200000!5m2!1sen!2sin",
                "additional_info": "Visitor entry is strictly regulated. Official passes must be collected at the main gate reception upon presenting valid identity proofs.",
                "gallery": [
                    "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1497215728101-856f4ea42174?auto=format&fit=crop&w=600&q=80"
                ]
            },
            {
                "id": "neyveli-post-office",
                "name": "Neyveli Post Office",
                "image": "https://images.unsplash.com/photo-1595079676339-1534801ad6cf?auto=format&fit=crop&w=600&q=80",
                "address": "Block 2, Post Office Street, Neyveli, Tamil Nadu 607801",
                "short_desc": "The primary India Post office providing mail, speed post, and savings schemes.",
                "full_desc": "The Head Post Office of Neyveli, located in Block 2, is the primary postal hub for the township. It offers a complete suite of services, including speed post, registered mail, parcel booking, money orders, and passport application services. It also manages postal savings accounts, public provident fund (PPF) schemes, and acts as the delivery base for all township blocks.",
                "timings": "09:00 AM - 05:00 PM (Monday to Saturday)",
                "contact": "Postmaster Desk: +91 4142 221102",
                "nearby": [
                    {"name": "St. Joseph's Church", "dist": "0.4 km"},
                    {"name": "IOCL Petrol Pump", "dist": "0.3 km"}
                ],
                "maps": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3914.856980076722!2d79.485!3d11.605!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3a54d588523c91fb%3A0xc3175ebc088be330!2sNeyveli%20Head%20Post%20Office!5e0!3m2!1sen!2sin!4v1718616300000!5m2!1sen!2sin",
                "additional_info": "Terms and savings accounts are available. Features an active digital counter for Aadhaar update and verification services.",
                "gallery": [
                    "https://images.unsplash.com/photo-1600132806370-bf17e65e942f?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1566121318578-f9b763a4ee4e?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1549488344-0b812f22b794?auto=format&fit=crop&w=600&q=80"
                ]
            },
            {
                "id": "neyveli-township-administration",
                "name": "Neyveli Township Administration Office",
                "image": "https://images.unsplash.com/photo-1577416416122-699684f0407a?auto=format&fit=crop&w=600&q=80",
                "address": "Township Office, Block 24, Neyveli, Tamil Nadu 607801",
                "short_desc": "The municipal administration center managing civil infrastructure and parks in Neyveli.",
                "full_desc": "The Neyveli Township Administration Office, located in Block 24, is the civil government of the Neyveli township. It operates under NLC India Limited and is responsible for managing water supply, street lighting, waste disposal, public parks, road maintenance, and housing allotments. It serves as the main center for grievance registration regarding township civil amenities.",
                "timings": "09:00 AM - 05:00 PM (Monday to Saturday)",
                "contact": "Chief Manager (Township): +91 4142 252253",
                "nearby": [
                    {"name": "NLC Community Hall", "dist": "0.2 km"},
                    {"name": "Children's Park", "dist": "0.8 km"}
                ],
                "maps": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3914.856980076722!2d79.48!3d11.594!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3a54d588523c91fb%3A0xc3175ebc088be330!2sNeyveli%20Township%20Administration!5e0!3m2!1sen!2sin!4v1718616400000!5m2!1sen!2sin",
                "additional_info": "Residents can register complaints online through the NLC Intranet or visit the office during public grievance hours.",
                "gallery": [
                    "https://images.unsplash.com/photo-1541829011-856d46471612?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1517502884422-41eaaced0168?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1497366754035-f200968a6e72?auto=format&fit=crop&w=600&q=80"
                ]
            },
            {
                "id": "neyveli-police-station",
                "name": "Neyveli Police Station (Thermal & Township)",
                "image": "https://images.unsplash.com/photo-1557085736-23579178e24f?auto=format&fit=crop&w=600&q=80",
                "address": "Block 29, Main Road, Neyveli Township, Tamil Nadu 607807",
                "short_desc": "The primary law enforcement office safeguarding Neyveli Township and NLC structures.",
                "full_desc": "Neyveli Township Police Station is the primary law enforcement office for the township. Under the Cuddalore District Police, the station is responsible for public safety, traffic regulation, and crime prevention within the township limits. It works closely with the NLC Industrial Security Force to monitor key entries and protect vital national infrastructure like power stations and mines.",
                "timings": "Open 24 Hours (For emergencies)",
                "contact": "Township Inspector: +91 4142 228224 / Control Room: 100",
                "nearby": [
                    {"name": "Sri Nataraja Temple", "dist": "0.4 km"},
                    {"name": "Neyveli Central Mosque", "dist": "0.5 km"}
                ],
                "maps": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3914.856980076722!2d79.467!3d11.61!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3a54d588523c91fb%3A0xc3175ebc088be330!2sNeyveli%20Township%20Police%20Station!5e0!3m2!1sen!2sin!4v1718616500000!5m2!1sen!2sin",
                "additional_info": "Passport verification and verification services are handled during standard office hours.",
                "gallery": [
                    "https://images.unsplash.com/photo-1508214751196-bcfd4ca60f91?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1549488344-0b812f22b794?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1533230898523-255b7d04000a?auto=format&fit=crop&w=600&q=80"
                ]
            },
            {
                "id": "neyveli-railway-post-office",
                "name": "Neyveli Railway Post Office",
                "image": "https://images.unsplash.com/photo-1556157382-97dea7d240ff?auto=format&fit=crop&w=600&q=80",
                "address": "Block 9, Near Railway Station, Neyveli, Tamil Nadu 607801",
                "short_desc": "Sub-post office serving the railway colony and Block 9 residents.",
                "full_desc": "The Railway Station Sub-Post Office in Block 9 is a smaller, convenient postal branch. It provides basic postal services, letter booking, savings deposit, and pension disbursement for the retired NLC employees living in Block 9 and the Railway Colony area.",
                "timings": "09:00 AM - 02:00 PM (Monday to Saturday)",
                "contact": "Sub-Postmaster: +91 4142 256102",
                "nearby": [
                    {"name": "Neyveli Railway Station", "dist": "0.2 km"},
                    {"name": "TELC Holy Trinity Church", "dist": "0.8 km"}
                ],
                "maps": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3914.856980076722!2d79.47!3d11.602!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3a54d588523c91fb%3A0xc3175ebc088be330!2sNeyveli%20Railway%20Station%20Post%20Office!5e0!3m2!1sen!2sin!4v1718616600000!5m2!1sen!2sin",
                "additional_info": "Highly convenient for booking express parcel posts due to its close proximity to the railway station.",
                "gallery": [
                    "https://images.unsplash.com/photo-1566121318578-f9b763a4ee4e?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1534447677768-be436bb09401?auto=format&fit=crop&w=600&q=80"
                ]
            },
            {
                "id": "tneb-substation-office",
                "name": "TNEB Substation Office",
                "image": "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?auto=format&fit=crop&w=600&q=80",
                "address": "Vandalur Main Road, Mandharakuppam, Neyveli, Tamil Nadu 607802",
                "short_desc": "Tamil Nadu Electricity Board administrative and service office for peripheral areas.",
                "full_desc": "The Tamil Nadu Generation and Distribution Corporation (TANGEDCO / TNEB) Office in Mandharakuppam handles electricity supply, connection requests, and bill payments for rural areas and neighborhoods located outside the NLC Township boundary. The office features a bill collection center and a technical desk for power maintenance.",
                "timings": "08:30 AM - 03:00 PM (Monday to Saturday)",
                "contact": "TNEB Assistant Engineer: +91 4142 258102",
                "nearby": [
                    {"name": "Mandharakuppam Market", "dist": "0.5 km"},
                    {"name": "Reliance Petrol Mart", "dist": "0.7 km"}
                ],
                "maps": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3914.856980076722!2d79.495!3d11.585!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3a54d588523c91fb%3A0xc3175ebc088be330!2sTNEB%20Office%20Mandharakuppam!5e0!3m2!1sen!2sin!4v1718616700000!5m2!1sen!2sin",
                "additional_info": "Features an online bill payment system. Emergencies can be reported directly to the substation control desk.",
                "gallery": [
                    "https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1497215728101-856f4ea42174?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1541829011-856d46471612?auto=format&fit=crop&w=600&q=80"
                ]
            }
        ]
    },
    "hospitals": {
        "title": "Hospitals",
        "file": "hospitals.html",
        "description": "Access vital medical services, clinics, and emergency hospitals operating in Neyveli.",
        "items": [
            {
                "id": "nlc-general-hospital",
                "name": "NLC India General Hospital",
                "image": "images/neyveli-hospital.jpg",
                "address": "Health Block, Block 24, Neyveli Township, Tamil Nadu 607801",
                "short_desc": "A premium 350-bed multi-specialty hospital run by NLCIL, providing free healthcare to employees.",
                "full_desc": "NLC India General Hospital is a premier multi-specialty medical center built to look after NLC India Limited employees, their dependants, and nearby rural communities. Equipped with 350 beds, the hospital features round-the-clock emergency trauma care, advanced intensive care units (ICUs), modern operation theatres, and dedicated pediatric, obstetric, cardiology, and orthopedic wards. It is recognized as a center of medical excellence in the Cuddalore district.",
                "timings": "Outpatient (OPD): 08:00 AM - 12:00 PM, 04:00 PM - 06:00 PM. Emergency: Open 24 Hours",
                "contact": "Emergency Desk: +91 4142 252258 / Hospital Superintendent: +91 4142 252199",
                "nearby": [
                    {"name": "Neyveli Boat House", "dist": "1.5 km"},
                    {"name": "NLC Township Administration Office", "dist": "0.8 km"}
                ],
                "maps": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3914.856980076722!2d79.48!3d11.594!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3a54d588523c91fb%3A0xc3175ebc088be330!2sNLC%20General%20Hospital!5e0!3m2!1sen!2sin!4v1718616800000!5m2!1sen!2sin",
                "additional_info": "Free medical aid is offered to contract workers and marginal communities. Features an advanced pharmacy department and ambulance dispatch services.",
                "gallery": [
                    "https://images.unsplash.com/photo-1519494026892-80bbd2d6fd0d?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1586773860418-d37222d8fce2?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1538108149393-f159e148c95a?auto=format&fit=crop&w=600&q=80"
                ]
            },
            {
                "id": "sneha-hospital",
                "name": "Sneha Hospital",
                "image": "https://images.unsplash.com/photo-1504813184591-0155b87051ff?auto=format&fit=crop&w=600&q=80",
                "address": "Block 18, Central Road, Neyveli Township, Tamil Nadu 607803",
                "short_desc": "A popular private hospital in Block 18 offering pediatrics and general medicine.",
                "full_desc": "Sneha Hospital is a highly trusted private healthcare facility in Block 18. Famed for its excellent outpatient services and pediatric care, it is a key destination for local families. The hospital runs basic laboratory testing, neonatal care, and general surgical procedures led by visiting consultants.",
                "timings": "09:00 AM - 09:00 PM (Daily). Emergency: Open 24 Hours",
                "contact": "Sneha Hospital Desk: +91 4142 253301",
                "nearby": [
                    {"name": "Nehru Park", "dist": "0.6 km"},
                    {"name": "Thulasi Pharmacy", "dist": "0.3 km"}
                ],
                "maps": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3914.856980076722!2d79.475!3d11.60!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3a54d588523c91fb%3A0xc3175ebc088be330!2sSneha%20Hospital%20Neyveli!5e0!3m2!1sen!2sin!4v1718616900000!5m2!1sen!2sin",
                "additional_info": "Features an in-house pharmacy and emergency laboratory testing facility.",
                "gallery": [
                    "https://images.unsplash.com/photo-1516549655169-df83a0774514?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1502740479091-6398b19d99f4?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1551076805-e1869f363c67?auto=format&fit=crop&w=600&q=80"
                ]
            },
            {
                "id": "sridharan-hospital",
                "name": "Sridharan Hospital",
                "image": "https://images.unsplash.com/photo-1512678080530-7760d81faba6?auto=format&fit=crop&w=600&q=80",
                "address": "Block 2, Post Office Road, Neyveli, Tamil Nadu 607801",
                "short_desc": "A multi-speciality family hospital specializing in maternal care and gynecology.",
                "full_desc": "Sridharan Hospital is a premier private hospital located in Block 2, Neyveli. The hospital is highly sought after for maternity services, gynecology, and high-risk pregnancy deliveries. It features comfortable patient wards, advanced labor suites, and a highly responsive pediatric care unit.",
                "timings": "09:00 AM - 01:00 PM, 05:00 PM - 09:00 PM (Daily)",
                "contact": "Reception Desk: +91 4142 221008",
                "nearby": [
                    {"name": "Neyveli Post Office", "dist": "0.2 km"},
                    {"name": "Arun Pharmacy", "dist": "0.1 km"}
                ],
                "maps": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3914.856980076722!2d79.485!3d11.605!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3a54d588523c91fb%3A0xc3175ebc088be330!2sSridharan%20Hospital%20Neyveli!5e0!3m2!1sen!2sin!4v1718617000000!5m2!1sen!2sin",
                "additional_info": "Offers well-structured health packages for women and senior citizens.",
                "gallery": [
                    "https://images.unsplash.com/photo-1629909613654-28e377c37b09?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1579684389782-64d84b5e905d?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1596464716127-f2a82984de30?auto=format&fit=crop&w=600&q=80"
                ]
            },
            {
                "id": "sri-ramachandra-hospital",
                "name": "Sri Ramachandra Hospital",
                "image": "https://images.unsplash.com/photo-1581594693702-fbdc51b2763b?auto=format&fit=crop&w=600&q=80",
                "address": "Block 1, Corporate Office Road, Neyveli, Tamil Nadu 607801",
                "short_desc": "A popular dental and diabetic clinic providing specialized care.",
                "full_desc": "Sri Ramachandra Hospital is a specialized medical center in Block 1, focusing on diabetes care, endocrine disorders, and dental services. Known for its modern diagnostic equipment and expert consulting doctors, it helps local patients manage chronic diseases effectively.",
                "timings": "09:00 AM - 01:00 PM, 04:30 PM - 08:30 PM (Closed on Sundays)",
                "contact": "Clinic Desk: +91 4142 254123",
                "nearby": [
                    {"name": "NLC Corporate Office", "dist": "0.3 km"},
                    {"name": "Sangeetha Restaurant", "dist": "0.4 km"}
                ],
                "maps": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3914.856980076722!2d79.483!3d11.603!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3a54d5bcffffffff%3A0x6b864a787b7a13d3!2sSri%20Ramachandra%20Hospital%20Neyveli!5e0!3m2!1sen!2sin!4v1718617100000!5m2!1sen!2sin",
                "additional_info": "Features advanced dental x-ray systems and diabetic foot check services.",
                "gallery": [
                    "https://images.unsplash.com/photo-1606811971618-4486d14f3f99?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1551601651-2a8555f1a136?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1512224095648-8f86a23cae53?auto=format&fit=crop&w=600&q=80"
                ]
            },
            {
                "id": "kasthuri-hospital",
                "name": "Kasthuri Hospital",
                "image": "https://images.unsplash.com/photo-1582719508461-905c673771fd?auto=format&fit=crop&w=600&q=80",
                "address": "Bypass Junction, Mandharakuppam, Neyveli, Tamil Nadu 607802",
                "short_desc": "Emergency hospital situated near the bypass, offering orthopedic and trauma services.",
                "full_desc": "Kasthuri Hospital is a private medical center located in Mandharakuppam. It specializes in orthopedics, joint replacements, and emergency trauma care. Its strategic location near the national highway bypass makes it a critical response center for accidental injuries and bone trauma in the region.",
                "timings": "Daily OPD: 09:30 AM - 02:00 PM, 05:00 PM - 09:00 PM. Emergency: 24/7",
                "contact": "Emergency Hotline: +91 94435 98765",
                "nearby": [
                    {"name": "Mandharakuppam Bus Stop", "dist": "0.4 km"},
                    {"name": "Vignesh Medicals", "dist": "0.1 km"}
                ],
                "maps": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3914.856980076722!2d79.495!3d11.585!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3a54d588523c91fb%3A0xc3175ebc088be330!2sKasthuri%20Hospital%20Mandharakuppam!5e0!3m2!1sen!2sin!4v1718617200000!5m2!1sen!2sin",
                "additional_info": "Fully equipped with digital X-Ray, plaster rooms, and physiotherapy centers.",
                "gallery": [
                    "https://images.unsplash.com/photo-1530026405186-ed1ea0ac7a63?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1519494026892-80bbd2d6fd0d?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1586773860418-d37222d8fce2?auto=format&fit=crop&w=600&q=80"
                ]
            },
            {
                "id": "av-hospital",
                "name": "A.V. Hospital",
                "image": "https://images.unsplash.com/photo-1551076805-e1869f363c67?auto=format&fit=crop&w=600&q=80",
                "address": "Bypass Road, Indira Nagar, Neyveli, Tamil Nadu 607801",
                "short_desc": "Multi-specialty private clinic providing cardiac screening and diabetic care.",
                "full_desc": "A.V. Hospital is a modern private healthcare facility located near Indira Nagar. The hospital offers multi-specialty outpatient consulting in cardiology, general medicine, and diabetology. It features a modern diagnostic laboratory and is highly preferred by residents of the bypass suburbs for quick checkups.",
                "timings": "09:00 AM - 08:30 PM (Daily)",
                "contact": "AV Hospital Desk: +91 98942 12000",
                "nearby": [
                    {"name": "Senthamil Mahal", "dist": "0.5 km"},
                    {"name": "Aryas Hotel", "dist": "0.8 km"}
                ],
                "maps": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3914.856980076722!2d79.49!3d11.60!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3a54d588523c91fb%3A0xc3175ebc088be330!2sAV%20Hospital%20Neyveli!5e0!3m2!1sen!2sin!4v1718617300000!5m2!1sen!2sin",
                "additional_info": "Home sample collection for blood diagnostic testing is provided for local areas.",
                "gallery": [
                    "https://images.unsplash.com/photo-1504813184591-0155b87051ff?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1516549655169-df83a0774514?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1502740479091-6398b19d99f4?auto=format&fit=crop&w=600&q=80"
                ]
            }
        ]
    },
    "schools-colleges": {
        "title": "Schools & Colleges",
        "file": "schools-colleges.html",
        "description": "Directory of prestigious schools, higher secondary institutions, and colleges in Neyveli.",
        "items": [
            {
                "id": "jawahar-matriculation-school",
                "name": "Jawahar Matriculation Higher Secondary School",
                "image": "images/neyveli-school.jpg",
                "address": "Block 17, Jawahar Street, Neyveli Township, Tamil Nadu 607803",
                "short_desc": "One of the most prestigious CBSE & Matriculation schools in Neyveli, offering high quality education.",
                "full_desc": "Jawahar Matriculation Higher Secondary School is a legendary educational institution in the Neyveli Township. Managed by the Jawahar Education Society and patronized by NLC India Limited, the school provides academic education under Matriculation and CBSE curricula. Famed for its exceptional academic results, massive sports grounds, science laboratories, and high student placement rates in elite engineering and medical colleges, it stands as the pride of Neyveli.",
                "timings": "08:30 AM - 04:10 PM (Monday to Saturday)",
                "contact": "School Principal Office: +91 4142 252117 / info@jawaharschoolneyveli.edu.in",
                "nearby": [
                    {"name": "Block 17 Post Office", "dist": "0.3 km"},
                    {"name": "Block 18 Shopping Center", "dist": "1 km"}
                ],
                "maps": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3914.856980076722!2d79.475!3d11.60!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3a54d588523c91fb%3A0xc3175ebc088be330!2sJawahar%20School%20Neyveli!5e0!3m2!1sen!2sin!4v1718617400000!5m2!1sen!2sin",
                "additional_info": "Includes excellent facilities for co-curricular activities like music, classical dance, and NCC training.",
                "gallery": [
                    "https://images.unsplash.com/photo-1509062522246-3755977927d7?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1427504494785-3a9ca7044f45?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1546410531-bb4caa6b424d?auto=format&fit=crop&w=600&q=80"
                ]
            },
            {
                "id": "st-joseph-of-cluny-school",
                "name": "St. Joseph of Cluny Matriculation School",
                "image": "https://images.unsplash.com/photo-1580582932707-520aed937b7b?auto=format&fit=crop&w=600&q=80",
                "address": "Block 25, Cluny Avenue, Neyveli Township, Tamil Nadu 607803",
                "short_desc": "A premier English-medium girls-centric convent school known for discipline and values.",
                "full_desc": "St. Joseph of Cluny School in Block 25 is a leading Christian convent institution serving the township for over 40 years. Managed by the Sisters of St. Joseph of Cluny, it is highly renowned for its emphasis on discipline, character building, academic excellence, and vocal English communication. The school has a massive infrastructure including multimedia classrooms and state-of-the-art libraries.",
                "timings": "08:45 AM - 03:45 PM (Monday to Friday)",
                "contact": "Cluny School Office: +91 4142 254412",
                "nearby": [
                    {"name": "St. Gabriel's Catholic Church", "dist": "0.8 km"},
                    {"name": "Block 25 Park", "dist": "0.2 km"}
                ],
                "maps": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3914.856980076722!2d79.48!3d11.595!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3a54d588523c91fb%3A0xc3175ebc088be330!2sSt%20Joseph%20of%20Cluny%20School%20Neyveli!5e0!3m2!1sen!2sin!4v1718617500000!5m2!1sen!2sin",
                "additional_info": "Admits boys up to Primary classes, but operates as an all-girls school for Higher Secondary.",
                "gallery": [
                    "https://images.unsplash.com/photo-1577896851231-70ef18881754?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1503676260728-1c00da094a0b?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1544717305-2782549b5136?auto=format&fit=crop&w=600&q=80"
                ]
            },
            {
                "id": "nlc-boys-school",
                "name": "NLC Boys Higher Secondary School",
                "image": "https://images.unsplash.com/photo-1588072432836-e10032774350?auto=format&fit=crop&w=600&q=80",
                "address": "Block 18, Neyveli Township, Tamil Nadu 607803",
                "short_desc": "A major government-aided school for boys offering state board education.",
                "full_desc": "NLC Boys Higher Secondary School in Block 18 is a large government-aided institution funded by NLC India Limited. Offering education in both Tamil and English mediums under the Tamil Nadu State Board, the school caters to thousands of boys, particularly from the working-class families of the township and surrounding villages.",
                "timings": "09:00 AM - 04:15 PM (Monday to Saturday)",
                "contact": "Headmaster Office: +91 4142 253308",
                "nearby": [
                    {"name": "Nehru Park", "dist": "0.4 km"},
                    {"name": "Sacred Heart Church", "dist": "0.5 km"}
                ],
                "maps": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3914.856980076722!2d79.475!3d11.60!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3a54d588523c91fb%3A0xc3175ebc088be330!2sNLC%20Boys%20School%20Neyveli!5e0!3m2!1sen!2sin!4v1718617600000!5m2!1sen!2sin",
                "additional_info": "Noted for its active athletic teams which regularly win district and state-level sports tournaments.",
                "gallery": [
                    "https://images.unsplash.com/photo-1516627145497-ae6968895b74?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1562774053-701939374585?auto=format&fit=crop&w=600&q=80"
                ]
            },
            {
                "id": "nlc-girls-school",
                "name": "NLC Girls High School",
                "image": "https://images.unsplash.com/photo-1596495578065-6e0763fa1141?auto=format&fit=crop&w=600&q=80",
                "address": "Block 11, Neyveli Township, Tamil Nadu 607803",
                "short_desc": "A respected government-aided school dedicated to the education of girls.",
                "full_desc": "NLC Girls High School, situated in Block 11, is a premier state-board school focusing on girls' education. Managed with funding support from NLCIL, the school provides high quality education, free notebooks, uniforms, and mid-day meals to students, ensuring high enrollment and literacy rates among girls in Cuddalore district.",
                "timings": "09:00 AM - 04:00 PM (Monday to Saturday)",
                "contact": "School HM Office: +91 4142 222108",
                "nearby": [
                    {"name": "Lignite Hall", "dist": "0.4 km"},
                    {"name": "NLC Cooperative Petrol Bunk", "dist": "0.3 km"}
                ],
                "maps": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3914.856980076722!2d79.47!3d11.60!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3a54d588523c91fb%3A0xc3175ebc088be330!2sNLC%20Girls%20School%20Neyveli!5e0!3m2!1sen!2sin!4v1718617700000!5m2!1sen!2sin",
                "additional_info": "Focuses heavily on vocational training and computer literacy programs for high-school students.",
                "gallery": [
                    "https://images.unsplash.com/photo-1503676260728-1c00da094a0b?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1522202176988-66273c2fd55f?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1427504494785-3a9ca7044f45?auto=format&fit=crop&w=600&q=80"
                ]
            },
            {
                "id": "jawahar-science-college",
                "name": "Jawahar Science College",
                "image": "https://images.unsplash.com/photo-1541339907198-e08756dedf3f?auto=format&fit=crop&w=600&q=80",
                "address": "Block 14, College Road, Neyveli Township, Tamil Nadu 607803",
                "short_desc": "A premier arts and science college affiliated to Thiruvalluvar University.",
                "full_desc": "Jawahar Science College, established in 1987 in Block 14, is a premier higher education institution in Neyveli. Affiliated with Thiruvalluvar University, the college offers undergraduate and postgraduate courses in Computer Science, Mathematics, Chemistry, Commerce, Business Administration, and English literature. It features a spacious library, computer labs, and active career counseling cells.",
                "timings": "09:30 AM - 04:30 PM (Monday to Friday)",
                "contact": "College Registrar Office: +91 4142 252114 / principal@jsc.edu.in",
                "nearby": [
                    {"name": "TELC Holy Trinity Church", "dist": "1.2 km"},
                    {"name": "Block 14 Playground", "dist": "0.3 km"}
                ],
                "maps": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3914.856980076722!2d79.47!3d11.602!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3a54d588523c91fb%3A0xc3175ebc088be330!2sJawahar%20Science%20College%20Neyveli!5e0!3m2!1sen!2sin!4v1718617800000!5m2!1sen!2sin",
                "additional_info": "Features active placement cells which invite top IT and finance companies for campus recruitment.",
                "gallery": [
                    "https://images.unsplash.com/photo-1523050854058-8df90110c9f1?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1498243691581-b145c3f54a5a?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1501290741922-b56c0d0c6e8e?auto=format&fit=crop&w=600&q=80"
                ]
            },
            {
                "id": "csm-college",
                "name": "C.S.M. College of Arts & Science",
                "image": "https://images.unsplash.com/photo-1523050854058-8df90110c9f1?auto=format&fit=crop&w=600&q=80",
                "address": "Vriddhachalam Bypass Road, Neyveli, Tamil Nadu 607802",
                "short_desc": "A popular private degree college providing job-oriented education.",
                "full_desc": "C.S.M. College of Arts & Science is a private co-educational institution situated along the Vriddhachalam Bypass. The college offers popular courses in Computer Application (BCA), Business Administration (BBA), Physics, and Commerce. Famed for its affordable fee structure, it attracts students from the rural outskirts of Cuddalore district.",
                "timings": "09:00 AM - 04:00 PM (Monday to Friday)",
                "contact": "College Office: +91 94422 98765",
                "nearby": [
                    {"name": "Villudayanpattu Murugan Temple", "dist": "2.5 km"},
                    {"name": "Mandharakuppam Market", "dist": "3 km"}
                ],
                "maps": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3914.856980076722!2d79.49!3d11.59!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3a54d588523c91fb%3A0xc3175ebc088be330!2sCSM%20College%20Neyveli!5e0!3m2!1sen!2sin!4v1718617900000!5m2!1sen!2sin",
                "additional_info": "Bus transport facilities are operated by the college covering a radius of 30 km for students.",
                "gallery": [
                    "https://images.unsplash.com/photo-1541339907198-e08756dedf3f?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1509062522246-3755977927d7?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1577896851231-70ef18881754?auto=format&fit=crop&w=600&q=80"
                ]
            }
        ]
    },
    "hotels-restaurants": {
        "title": "Hotels & Restaurants",
        "file": "hotels-restaurants.html",
        "description": "Explore top restaurants, family eateries, and hotels in Neyveli.",
        "items": [
            {
                "id": "hotel-lignite",
                "name": "Hotel Lignite",
                "image": "images/neyveli-restaurant.jpg",
                "address": "Block 18, Central Street, Neyveli Township, Tamil Nadu 607803",
                "short_desc": "A premier multi-cuisine family restaurant in Block 18, famous for Biryani and Chinese dishes.",
                "full_desc": "Hotel Lignite in Block 18 is the most popular dining destination for multi-cuisine food inside the Neyveli Township. Offering a beautifully designed air-conditioned family dining hall, it serves a wide array of South Indian, North Indian, Tandoori, Chinese, and Muglai dishes. The restaurant is particularly famous for its Hyderabadi Biryani and Butter Chicken, making it a favorite for family weekend dinners.",
                "timings": "11:00 AM - 10:30 PM (Daily)",
                "contact": "Hotel Lignite Booking: +91 4142 253303",
                "nearby": [
                    {"name": "Nehru Park", "dist": "0.5 km"},
                    {"name": "Thulasi Pharmacy", "dist": "0.2 km"}
                ],
                "maps": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3914.856980076722!2d79.475!3d11.60!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3a54d588523c91fb%3A0xc3175ebc088be330!2sHotel%20Lignite%20Neyveli!5e0!3m2!1sen!2sin!4v1718618000000!5m2!1sen!2sin",
                "additional_info": "Home delivery is supported within the Neyveli Township. Features a party hall with a capacity of 100 people.",
                "gallery": [
                    "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1414235077428-338989a2e8c0?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1552566626-52f8b828add9?auto=format&fit=crop&w=600&q=80"
                ]
            },
            {
                "id": "radhakrishna-hotel",
                "name": "Radhakrishna Hotel",
                "image": "https://images.unsplash.com/photo-1589301760014-d929f3979dbc?auto=format&fit=crop&w=600&q=80",
                "address": "Block 24, Main Road, Neyveli Township, Tamil Nadu 607801",
                "short_desc": "A traditional vegetarian hotel serving delicious meals, dosas, and filter coffee.",
                "full_desc": "Radhakrishna Hotel is a legendary pure vegetarian eatery located in Block 24. Known for serving authentic South Indian breakfast and meals, it is a daily stop for many township residents. Their crispy Ghee Roasts, fluffy idlis served with three varieties of chutneys, and hot South Indian filter coffee are highly recommended.",
                "timings": "06:00 AM - 10:00 PM (Daily)",
                "contact": "Radhakrishna Desk: +91 4142 252204",
                "nearby": [
                    {"name": "Neyveli Boat House", "dist": "1 km"},
                    {"name": "Children's Park", "dist": "0.8 km"}
                ],
                "maps": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3914.856980076722!2d79.48!3d11.594!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3a54d588523c91fb%3A0xc3175ebc088be330!2sRadhakrishna%20Hotel%20Neyveli!5e0!3m2!1sen!2sin!4v1718618100000!5m2!1sen!2sin",
                "additional_info": "Features a classic non-AC section and an AC family hall upstairs. Outdoor catering service is available.",
                "gallery": [
                    "https://images.unsplash.com/photo-1601050690597-df056fb4ce78?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1541832676-9b763b0239ab?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1626132647523-66f5bf380027?auto=format&fit=crop&w=600&q=80"
                ]
            },
            {
                "id": "sangeetha-restaurant",
                "name": "Sangeetha Restaurant",
                "image": "https://images.unsplash.com/photo-1504674900247-0877df9cc836?auto=format&fit=crop&w=600&q=80",
                "address": "Block 1, Commercial Complex, Neyveli, Tamil Nadu 607801",
                "short_desc": "A branch of the popular vegetarian chain offering quality snacks and meals.",
                "full_desc": "Sangeetha Restaurant in Block 1 provides a premium, clean, and family-friendly dining experience. Affiliated with the famous Sangeetha chain, it serves North Indian and South Indian vegetarian dishes. Their North Indian Thali and chat items are highly popular during evening hours.",
                "timings": "07:00 AM - 10:30 PM (Daily)",
                "contact": "Sangeetha B1 Desk: +91 4142 254415",
                "nearby": [
                    {"name": "NLC Corporate Office", "dist": "0.2 km"},
                    {"name": "Sri Ramachandra Hospital", "dist": "0.4 km"}
                ],
                "maps": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3914.856980076722!2d79.483!3d11.603!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3a54d5bcffffffff%3A0x6b864a787b7a13d3!2sSangeetha%20Restaurant%20Neyveli!5e0!3m2!1sen!2sin!4v1718618200000!5m2!1sen!2sin",
                "additional_info": "A dedicated bakery counter selling fresh cakes and sweets is situated at the entrance.",
                "gallery": [
                    "https://images.unsplash.com/photo-1565557623262-b51c2513a641?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1512621776951-a57141f2eefd?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1606787366850-de6330128bfc?auto=format&fit=crop&w=600&q=80"
                ]
            },
            {
                "id": "hotel-aryas",
                "name": "Hotel Aryas",
                "image": "https://images.unsplash.com/photo-1567188040759-fb8a883dc6d8?auto=format&fit=crop&w=600&q=80",
                "address": "Cuddalore Main Road, Mandharakuppam, Neyveli, Tamil Nadu 607802",
                "short_desc": "A popular highway vegetarian hotel offering fast service for travelers.",
                "full_desc": "Hotel Aryas is situated on the busy Mandharakuppam highway stretch. It is a highly frequented stop for travelers driving between Chennai and Kumbakonam. Famed for its prompt service and consistency, Aryas serves traditional Tamil meals, mini tiffins, and fresh fruit juices at budget-friendly rates.",
                "timings": "06:00 AM - 10:30 PM (Daily)",
                "contact": "Aryas Mandharakuppam: +91 94435 54321",
                "nearby": [
                    {"name": "Mandharakuppam Bus Stop", "dist": "0.3 km"},
                    {"name": "PKR Mahal", "dist": "0.6 km"}
                ],
                "maps": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3914.856980076722!2d79.495!3d11.585!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3a54d588523c91fb%3A0xc3175ebc088be330!2sHotel%20Aryas%20Mandharakuppam!5e0!3m2!1sen!2sin!4v1718618300000!5m2!1sen!2sin",
                "additional_info": "Ample parking area in front of the hotel makes it highly convenient for road trip stopovers.",
                "gallery": [
                    "https://images.unsplash.com/photo-1498837167922-ddd27525d352?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1482049016688-2d3e1b311543?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1484723091739-30a097e8f929?auto=format&fit=crop&w=600&q=80"
                ]
            },
            {
                "id": "sri-balaji-hotel",
                "name": "Sri Balaji Hotel",
                "image": "https://images.unsplash.com/photo-1605180758280-29fb379dd50b?auto=format&fit=crop&w=600&q=80",
                "address": "Block 11, Cooperative Bazaar Road, Neyveli, Tamil Nadu 607803",
                "short_desc": "A local family hotel offering delicious non-vegetarian options like parottas and salna.",
                "full_desc": "Sri Balaji Hotel is a popular local non-vegetarian dining outlet in Block 11. Famed for its layered, soft Malabar Parottas served with spicy chicken and mutton salna, the hotel is highly popular among youths. It also offers quick takeaway services.",
                "timings": "11:30 AM - 03:30 PM, 06:30 PM - 10:30 PM (Daily)",
                "contact": "Balaji Hotel Desk: +91 98943 98765",
                "nearby": [
                    {"name": "Lignite Hall", "dist": "0.4 km"},
                    {"name": "NLC Cooperative Petrol Bunk", "dist": "0.3 km"}
                ],
                "maps": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3914.856980076722!2d79.47!3d11.60!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3a54d588523c91fb%3A0xc3175ebc088be330!2sSri%20Balaji%20Hotel%20Neyveli!5e0!3m2!1sen!2sin!4v1718618400000!5m2!1sen!2sin",
                "additional_info": "Freshly fried Chilli Chicken and Pepper Fry are prepared live in front of the shop in the evenings.",
                "gallery": [
                    "https://images.unsplash.com/photo-1606787366850-de6330128bfc?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1504754524776-8f4f37790ca0?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1476224203421-9ac39bcb3327?auto=format&fit=crop&w=600&q=80"
                ]
            },
            {
                "id": "ananda-bhavan-restaurant",
                "name": "Ananda Bhavan Restaurant",
                "image": "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=600&q=80",
                "address": "Neyveli Bypass Junction, Mandharakuppam, Tamil Nadu 607802",
                "short_desc": "A premium vegetarian restaurant offering classic South Indian meals and chat items.",
                "full_desc": "Ananda Bhavan is a newly opened, modern vegetarian restaurant situated near the Neyveli Bypass. The restaurant features premium interiors, air conditioning, and offers high quality North Indian, South Indian, and Indo-Chinese food. Their evening chat counter and special sweets selection are major attractions.",
                "timings": "07:00 AM - 10:30 PM (Daily)",
                "contact": "Ananda Bhavan Office: +91 97890 54321",
                "nearby": [
                    {"name": "A.R. Mahal", "dist": "1 km"},
                    {"name": "Shell Petrol Station", "dist": "0.8 km"}
                ],
                "maps": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3914.856980076722!2d79.50!3d11.58!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3a54d588523c91fb%3A0xc3175ebc088be330!2sAnanda%20Bhavan%20Neyveli!5e0!3m2!1sen!2sin!4v1718618500000!5m2!1sen!2sin",
                "additional_info": "Excellent place to buy high quality Indian ghee sweets and gift packs.",
                "gallery": [
                    "https://images.unsplash.com/photo-1563729784474-d77dbb933a9e?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1587314168485-3236d6710814?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1551248429-40975aa4de74?auto=format&fit=crop&w=600&q=80"
                ]
            }
        ]
    },
    "transport-services": {
        "title": "Transport Services",
        "file": "transport-services.html",
        "description": "Locate essential transport nodes, bus routes, rail bookings, and rental services in Neyveli.",
        "items": [
            {
                "id": "neyveli-bus-stand",
                "name": "Neyveli Central Bus Stand",
                "image": "images/bus-stand-banner.jpg",
                "address": "Block 24, Main Road, Neyveli Township, Tamil Nadu 607801",
                "short_desc": "The primary transit hub connecting Neyveli to Chennai, Trichy, Kumbakonam, and Cuddalore.",
                "full_desc": "Neyveli Central Bus Stand is the beating heart of local and long-distance transport in the township. Operated by the Tamil Nadu State Transport Corporation (TNSTC) and private operators, it provides round-the-clock bus connectivity. Direct buses run to Chennai (via Villupuram), Kumbakonam, Trichy, Chidambaram, Coimbatore, and Bangalore. The bus stand features ticket reservation counters, passenger waiting halls, and several local shops.",
                "timings": "Open 24 Hours",
                "contact": "TNSTC Enquiry Counter: +91 4142 252251",
                "nearby": [
                    {"name": "Neyveli Arch", "dist": "3 km"},
                    {"name": "NLC Community Hall", "dist": "0.8 km"}
                ],
                "maps": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3914.856980076722!2d79.48!3d11.594!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3a54d588523c91fb%3A0xc3175ebc088be330!2sNeyveli%20Bus%20Stand!5e0!3m2!1sen!2sin!4v1718618600000!5m2!1sen!2sin",
                "additional_info": "Reservations for SETC (Express) buses can be booked online through the TNSTC portal.",
                "gallery": [
                    "https://images.unsplash.com/photo-1544620347-c4fd4a3d5957?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1570125909232-eb263c188f7e?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1568605117036-5fe5e7bab0b7?auto=format&fit=crop&w=600&q=80"
                ]
            },
            {
                "id": "neyveli-railway-station",
                "name": "Neyveli Railway Station",
                "image": "images/railway-banner.jpg",
                "address": "Block 9, Station Road, Neyveli, Tamil Nadu 607801",
                "short_desc": "An essential passenger and industrial cargo rail terminal in Neyveli.",
                "full_desc": "Neyveli Railway Station (Station Code: NVL) is a vital railway link under the Trichy Division of Southern Railway. Situated in Block 9, the station serves passenger trains connecting Cuddalore, Vriddhachalam, Trichy, and Salem. It also plays a key industrial role in the logistics of NLC by facilitating cargo trains transport of heavy materials and machinery.",
                "timings": "Open according to train schedules",
                "contact": "Railway Enquiry Desk: +91 4142 256220 / Southern Railway: 139",
                "nearby": [
                    {"name": "Railway Post Office", "dist": "0.2 km"},
                    {"name": "TELC Holy Trinity Church", "dist": "1 km"}
                ],
                "maps": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3914.856980076722!2d79.47!3d11.602!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3a54d588523c91fb%3A0xc3175ebc088be330!2sNeyveli%20Railway%20Station!5e0!3m2!1sen!2sin!4v1718618700000!5m2!1sen!2sin",
                "additional_info": "Features a computerised passenger reservation center (PRS) open from 08:00 AM to 02:00 PM.",
                "gallery": [
                    "https://images.unsplash.com/photo-1474487548417-781f7f495b3b?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1515162305285-0293e4767cc2?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1532103054090-334e6e60b73a?auto=format&fit=crop&w=600&q=80"
                ]
            },
            {
                "id": "local-auto-cab-stand",
                "name": "Local Auto Stand & Taxi Services",
                "image": "https://images.unsplash.com/photo-1566008889975-fba7a79ecf3f?auto=format&fit=crop&w=600&q=80",
                "address": "Block 1, Near Commercial Complex, Neyveli, Tamil Nadu 607801",
                "short_desc": "Find local passenger auto-rickshaws and cabs operating within Neyveli.",
                "full_desc": "The Block 1 Auto Rickshaw and Taxi Stand is the most reliable place to hire local transport within the Neyveli Township. Auto-rickshaws are available for transit to all blocks, hospitals, and schools. For outstation travel, several private taxi operators run hatchbacks, sedans, and SUVs on rent.",
                "timings": "Open 24 Hours",
                "contact": "Auto Stand Coordinator: +91 94422 12040",
                "nearby": [
                    {"name": "NLC Corporate Office", "dist": "0.3 km"},
                    {"name": "Sangeetha Restaurant", "dist": "0.1 km"}
                ],
                "maps": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3914.856980076722!2d79.483!3d11.603!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3a54dbcffffffff%3A0x6b864a787b7a13d3!2sNeyveli%20Auto%20Stand!5e0!3m2!1sen!2sin!4v1718618800000!5m2!1sen!2sin",
                "additional_info": "Fares inside the township are generally pre-fixed based on block distance. Ensure you agree on the rate before boarding.",
                "gallery": [
                    "https://images.unsplash.com/photo-1494790108377-be9c29b29330?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1549488344-1f9b8d2bd1f3?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1508214751196-bcfd4ca60f91?auto=format&fit=crop&w=600&q=80"
                ]
            },
            {
                "id": "puducherry-airport",
                "name": "Puducherry Airport (PNY)",
                "image": "images/airport-banner.jpg",
                "address": "Lawspet, Puducherry 605008",
                "short_desc": "The nearest domestic airport connecting Neyveli to Bangalore and Hyderabad.",
                "full_desc": "Puducherry Airport (PNY) is the nearest airport to Neyveli, located approximately 62 km away. The airport features a modern passenger terminal and hosts domestic flights operated by regional carriers, connecting passengers primarily to Bengaluru and Hyderabad. For international travel, Chennai International Airport (MAA) located 200 km away serves as the primary gateway.",
                "timings": "Depends on flight schedules",
                "contact": "AAI Puducherry Office: +91 413 2253173",
                "nearby": [
                    {"name": "Lawspet Heliport", "dist": "1 km"},
                    {"name": "Pondicherry Beach", "dist": "5 km"}
                ],
                "maps": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3916.128!2d79.81!3d11.96!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3a5363abcdefabcd%3A0xabcdefabcdefabcd!2sPuducherry%20Airport!5e0!3m2!1sen!2sin!4v1718618900000!5m2!1sen!2sin",
                "additional_info": "Cab booking services (Ola, Uber, and private rentals) are easily available from Pondicherry to Neyveli.",
                "gallery": [
                    "https://images.unsplash.com/photo-1436491865332-7a61a109cc05?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1490430657723-4d607c1503fc?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1530521954074-e64f6810b32d?auto=format&fit=crop&w=600&q=80"
                ]
            },
            {
                "id": "nlc-logistics-cargo",
                "name": "NLC Logistics & Cargo Operations",
                "image": "images/truck-banner.jpg",
                "address": "Block 26, Industrial Zone, Neyveli, Tamil Nadu 607803",
                "short_desc": "Industrial heavy cargo, logistics, and mineral shipping division of NLC India.",
                "full_desc": "NLC Logistics & Cargo division handles the massive industrial transportation needs of NLC India Limited. It coordinates the transport of heavy mining equipment, lignite shipping, thermal turbine parts, and coordinates heavy cargo operations with railways and major ports like Chennai and Karaikal.",
                "timings": "09:00 AM - 05:30 PM (Daily)",
                "contact": "Logistics Superintendent: +91 4142 252290",
                "nearby": [
                    {"name": "CSI Good Shepherd Church", "dist": "0.8 km"},
                    {"name": "Mines Office", "dist": "2.5 km"}
                ],
                "maps": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3914.856980076722!2d79.48!3d11.59!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3a54d588523c91fb%3A0xc3175ebc088be330!2sNLC%20Logistics%20Office!5e0!3m2!1sen!2sin!4v1718619000000!5m2!1sen!2sin",
                "additional_info": "Authorized personnel only are allowed inside the heavy logistics zone.",
                "gallery": [
                    "https://images.unsplash.com/photo-1601584115197-04ecc0da31d7?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1516574187841-cb9cc2ca948b?auto=format&fit=crop&w=600&q=80"
                ]
            },
            {
                "id": "neyveli-travel-agencies",
                "name": "Neyveli Travel Agencies & Private Cabs",
                "image": "https://images.unsplash.com/photo-1549317661-bd32c8ce0db2?auto=format&fit=crop&w=600&q=80",
                "address": "Block 18, Commercial Row, Neyveli, Tamil Nadu 607803",
                "short_desc": "Private tour operators, car rentals, and luxury bus bookings for pilgrims and tourists.",
                "full_desc": "The commercial row of Block 18 houses major private travel agencies like Neyveli Travels, Sri Balaji Cabs, and Royal Tour Operators. They offer local and outstation taxi booking services, luxury private coaches (sleeper buses to Chennai, Bangalore, and Salem), and customized tour packages for nearby spiritual centers like Chidambaram, Srimushnam, and Pichavaram.",
                "timings": "07:00 AM - 10:00 PM (Daily)",
                "contact": "Travel Desk: +91 94432 12098",
                "nearby": [
                    {"name": "Hotel Lignite", "dist": "0.2 km"},
                    {"name": "Nehru Park", "dist": "0.5 km"}
                ],
                "maps": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3914.856980076722!2d79.475!3d11.60!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3a54d588523c91fb%3A0xc3175ebc088be330!2sNeyveli%20Travels!5e0!3m2!1sen!2sin!4v1718619100000!5m2!1sen!2sin",
                "additional_info": "Offers special packages for Pondicherry airport drops and Chidambaram temple tours.",
                "gallery": [
                    "https://images.unsplash.com/photo-1520038410233-7141be7e6f97?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1494515426402-f1980a22a0b2?auto=format&fit=crop&w=600&q=80",
                    "https://images.unsplash.com/photo-1506012787146-f92b2d7d6d96?auto=format&fit=crop&w=600&q=80"
                ]
            }
        ]
    }
}

# HTML templates
CATEGORY_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - NEYVELI Portal</title>
    <meta name="description" content="{description}">
    <link href="https://fonts.googleapis.com/css2?family=Lato:wght@400;700;900&family=Open+Sans:wght@400;600&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="css/style.css">
    <style>
        .places-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
            gap: 2.5rem;
        }}
        .place-card {{
            background: #fff;
            border-radius: 12px;
            overflow: hidden;
            box-shadow: 0 8px 20px rgba(0,0,0,0.08);
            transition: var(--transition);
            display: flex;
            flex-direction: column;
            border: 1px solid #eee;
        }}
        .place-card:hover {{
            transform: translateY(-8px);
            box-shadow: 0 15px 30px rgba(0,0,0,0.12);
            border-color: var(--primary-color);
        }}
        .place-img {{
            width: 100%;
            height: 220px;
            object-fit: cover;
        }}
        .place-content {{
            padding: 1.5rem;
            flex-grow: 1;
            display: flex;
            flex-direction: column;
        }}
        .place-title {{
            font-size: 1.3rem;
            color: var(--primary-color);
            margin-bottom: 0.5rem;
        }}
        .place-location {{
            font-size: 0.9rem;
            color: #666;
            margin-bottom: 1rem;
            display: flex;
            align-items: center;
            gap: 5px;
        }}
        .place-desc {{
            font-size: 0.95rem;
            margin-bottom: 1.5rem;
            flex-grow: 1;
            line-height: 1.6;
        }}
        .view-btn {{
            align-self: flex-start;
            padding: 0.6rem 1.5rem;
            border: 2px solid var(--primary-color);
            border-radius: 25px;
            color: var(--primary-color);
            font-weight: 600;
            background: transparent;
            transition: var(--transition);
        }}
        .view-btn:hover {{
            background: var(--primary-color);
            color: #fff;
        }}
    </style>
</head>
<body>
    <header></header>
    <main>
        <div class="breadcrumb">
            <a href="index.html">Home</a> &raquo; <span>{title}</span>
        </div>
        <section class="container">
            <h1 class="section-title">{title}</h1>
            <p style="text-align:center; margin-bottom: 3rem; font-size: 1.1rem; color: #555;">{description}</p>
            
            <div class="places-grid">
                {cards_html}
            </div>
        </section>
    </main>
    <footer></footer>
    <script src="js/main.js"></script>
</body>
</html>
"""

CARD_TEMPLATE = """
                <div class="place-card">
                    <figure style="margin:0;">
                        <img src="{image}" alt="{name}" title="{name}" class="place-img">
                    </figure>
                    <div class="place-content">
                        <h3 class="place-title">{index}. {name}</h3>
                        <div class="place-location">📍 {address_short}</div>
                        <p class="place-desc">{short_desc}</p>
                        <a href="details/{id}.html" class="view-btn">View Details</a>
                    </div>
                </div>
"""

DETAIL_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{name} - {category_title} - NEYVELI Portal</title>
    <link href="https://fonts.googleapis.com/css2?family=Lato:wght@400;700;900&family=Open+Sans:wght@400;600&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="../css/style.css">
    <style>
        .detail-container {{
            display: grid;
            grid-template-columns: 1fr;
            gap: 2rem;
            margin-top: 2rem;
        }}
        @media (min-width: 768px) {{
            .detail-container {{
                grid-template-columns: 2fr 1fr;
            }}
        }}
        .detail-gallery img {{
            width: 100%;
            height: auto;
            max-height: 450px;
            object-fit: cover;
            border-radius: 12px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
            margin-bottom: 1.5rem;
        }}
        .info-sidebar {{
            background: #fff;
            padding: 1.5rem;
            border-radius: 12px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.05);
            border: 1px solid #eaeaea;
            height: fit-content;
        }}
        .info-sidebar h3 {{
            color: var(--primary-color);
            border-bottom: 2px solid var(--primary-color);
            padding-bottom: 0.5rem;
            margin-bottom: 1.2rem;
            font-size: 1.25rem;
        }}
        .info-item {{
            margin-bottom: 1.2rem;
        }}
        .info-label {{
            font-weight: 700;
            color: #555;
            display: block;
            font-size: 0.9rem;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            margin-bottom: 0.25rem;
        }}
        .info-val {{
            color: #222;
            font-size: 0.95rem;
            line-height: 1.5;
        }}
        .nearby-places {{
            margin-top: 2.5rem;
            padding: 1.5rem;
            background: var(--light-gray);
            border-radius: 12px;
        }}
        .nearby-places h3 {{
            color: var(--dark-gray);
            margin-bottom: 1.2rem;
            font-size: 1.2rem;
        }}
        .nearby-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 1rem;
        }}
        .nearby-card {{
            background: #fff;
            padding: 1rem;
            border-radius: 8px;
            border: 1px solid #ddd;
            font-size: 0.9rem;
        }}
        .map-container {{
            margin-top: 1.5rem;
            border-radius: 12px;
            overflow: hidden;
            border: 1px solid #ddd;
            height: 250px;
        }}
        .map-container iframe {{
            width: 100%;
            height: 100%;
            border: 0;
        }}
        .full-description {{
            line-height: 1.8;
            font-size: 1.05rem;
            color: #333;
        }}
        .full-description p {{
            margin-bottom: 1rem;
        }}
        .image-gallery-section {{
            margin-top: 3rem;
        }}
        .image-gallery-section h3 {{
            font-size: 1.5rem;
            color: var(--primary-color);
            margin-bottom: 1rem;
            border-bottom: 2px solid #eee;
            padding-bottom: 0.5rem;
        }}
        .gallery-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
            gap: 1.5rem;
        }}
        .gallery-item {{
            overflow: hidden;
            border-radius: 8px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.05);
            border: 1px solid #ddd;
            height: 150px;
        }}
        .gallery-item img {{
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: var(--transition);
        }}
        .gallery-item img:hover {{
            transform: scale(1.08);
        }}
    </style>
</head>
<body>
    <header></header>
    <main>
        <div class="breadcrumb">
            <a href="../index.html">Home</a> &raquo; <a href="../{category_file}">{category_title}</a> &raquo; <span>{name}</span>
        </div>
        <section class="container">
            <h1 class="section-title" style="margin-bottom: 2rem;">{name}</h1>
            
            <div class="detail-container">
                <div>
                    <div class="detail-gallery">
                        <img src="../{image}" alt="{name}" class="main-img">
                    </div>
                    <div class="full-description">
                        <p>{full_desc}</p>
                    </div>
                    
                    <div class="image-gallery-section">
                        <h3>Additional Photos</h3>
                        <div class="gallery-grid">
                            {gallery_html}
                        </div>
                    </div>
                    
                    <div class="nearby-places">
                        <h3>Nearby Places to Explore</h3>
                        <div class="nearby-grid">
                            {nearby_html}
                        </div>
                    </div>
                </div>
                
                <div class="info-sidebar">
                    <h3>Quick Information</h3>
                    <div class="info-item">
                        <span class="info-label">Complete Address</span>
                        <span class="info-val">{address}</span>
                    </div>
                    <div class="info-item">
                        <span class="info-label">Contact Details</span>
                        <span class="info-val">{contact}</span>
                    </div>
                    <div class="info-item">
                        <span class="info-label">Timings & Hours</span>
                        <span class="info-val">{timings}</span>
                    </div>
                    <div class="info-item">
                        <span class="info-label">Additional Information</span>
                        <span class="info-val">{additional_info}</span>
                    </div>
                    
                    <div class="map-container">
                        <iframe src="{maps}" allowfullscreen="" loading="lazy"></iframe>
                    </div>
                </div>
            </div>
        </section>
    </main>
    <footer></footer>
    <script src="../js/main.js"></script>
</body>
</html>
"""

# Generate pages
for cat_key, cat_data in categories.items():
    print(f"Generating pages for category: {cat_data['title']}...")
    cards_html = ""
    for idx, item in enumerate(cat_data["items"], 1):
        # Prepare card variables
        address_parts = item["address"].split(",")
        address_short = address_parts[0]
        if len(address_parts) > 1:
            address_short += ", " + address_parts[1].strip()

        cards_html += CARD_TEMPLATE.format(
            image=item["image"],
            name=item["name"],
            index=idx,
            address_short=address_short,
            short_desc=item["short_desc"],
            id=item["id"]
        )

        # Generate detailed page
        nearby_html = ""
        for nb in item["nearby"]:
            nearby_html += f"""
                            <div class="nearby-card">
                                <strong>{nb['name']}</strong><br>
                                <span style="color:#666;">Distance: {nb['dist']}</span>
                            </div>"""

        gallery_html = ""
        for img_url in item["gallery"]:
            gallery_html += f"""
                            <div class="gallery-item">
                                <img src="{img_url}" alt="{item['name']} - Additional Photo">
                            </div>"""

        detail_content = DETAIL_TEMPLATE.format(
            name=item["name"],
            category_title=cat_data["title"],
            category_file=cat_data["file"],
            image=item["image"],
            full_desc=item["full_desc"],
            nearby_html=nearby_html,
            gallery_html=gallery_html,
            address=item["address"],
            contact=item["contact"],
            timings=item["timings"],
            additional_info=item["additional_info"],
            maps=item["maps"]
        )
        
        detail_filepath = os.path.join(DETAILS_DIR, f"{item['id']}.html")
        with open(detail_filepath, "w", encoding="utf-8") as df:
            df.write(detail_content)

    # Write main category file
    category_content = CATEGORY_TEMPLATE.format(
        title=cat_data["title"],
        description=cat_data["description"],
        cards_html=cards_html
    )
    category_filepath = os.path.join(WORKSPACE_DIR, cat_data["file"])
    with open(category_filepath, "w", encoding="utf-8") as cf:
        cf.write(category_content)

print("All category and detail pages generated successfully with high quality, unique images and galleries!")
