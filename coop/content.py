"""SOEMCO website content, copied from https://www.soemco.org.ph (October 2026).

`python manage.py seed` loads this into the database; `python manage.py import_photos`
downloads the images and form files listed here. After that, edit everything in /admin/.
Image and file paths are relative to https://www.soemco.org.ph/wp-content/uploads/.
"""
from datetime import date

UPLOADS = "https://www.soemco.org.ph/wp-content/uploads/"
LOGO = "2025/04/favicon.png"

# ---------------------------------------------------------------- Branches
SDN, SDS, ADN = "Surigao del Norte", "Surigao del Sur", "Agusan del Norte"
BRANCHES = [
    # name, province, address, head, map, is_main, photo
    ("Central Office", SDN, "A. Lasala St., Brgy. Navarro, Socorro, Surigao del Norte", "Dante M. Deliman",
     "https://maps.app.goo.gl/79x734ZHyBZX1ofSA", True, "2025/09/SOCORRO160-scaled.jpg"),
    ("Alegria", SDN, "Brgy. Poblacion, Alegria, Surigao del Norte", "Angelito R. Jualo",
     "https://maps.app.goo.gl/5kvSihdgHVMebwRZA", False, "2025/09/1739265939936-scaled.jpg"),
    ("Claver", SDN, "Rizal St., P-6, Brgy. Tayaga, Claver, Surigao del Norte", "Richard P. Dizon",
     "https://maps.app.goo.gl/zYEtVmASH2YrocFV6", False, "2025/09/1739268990513-scaled.jpg"),
    ("Dapa", SDN, "Brgy. 12, Poblacion, Dapa, Surigao del Norte", "Nathaniel B. Mondragon",
     "https://maps.app.goo.gl/N9cNeZTbyvFJ8PXAA", False, "2025/09/DAPA00-scaled.jpg"),
    ("Sta. Monica Satellite", SDN, "Brgy. T. Arlan, Sta. Monica, Siargao, Surigao del Norte", "Jeo Ann D. Jugar",
     "https://maps.app.goo.gl/tkhtopcrEscnudfB9", False, "2025/09/SAPAO-20-scaled.jpg"),
    ("Surigao City", SDN, "Gemina St., Brgy. Washington, Surigao City, Surigao del Norte", "Hadjie B. Cordita",
     "https://maps.app.goo.gl/WhYRhiqxYp5TLU4q6", False, "2025/09/1739269869432-1-scaled.jpg"),
    ("Bislig", SDS, "R.B. Castillo St., Brgy. Mangagoy, Bislig, Surigao del Sur", "Junmark B. Sutana",
     "https://maps.app.goo.gl/kcjHNHDkzcUz2yGE9", False, "2025/11/bislig_branch.png"),
    ("Cantilan", SDS, "La Purisima St., Cantilan, Surigao del Sur", "Joemar J. Ramirez",
     "https://maps.app.goo.gl/T8uZZ9i6hExewTVs7", False, "2025/09/1739268057484-scaled.jpg"),
    ("Tandag", SDS, "Osmeña St., Brgy. Bag-ong Lungsod, Tandag City, Surigao del Sur", "Jenny E. Golgat",
     "https://maps.app.goo.gl/RHTHBoYcwkkfhcxn6", False, "2025/09/1739271332286-scaled.jpg"),
    ("Butuan", ADN, "North Montilla Blvd., San Juan, Butuan City, Agusan del Norte", "Dean Lumangcas",
     "https://maps.app.goo.gl/hszpo3WFW8kdUPPA6", False, "2025/09/1739266958497-scaled.jpg"),
    ("Cabadbaran", ADN, "Asis St., Pob. 8, Cabadbaran City, Agusan del Norte", "Jobane Pajoyo",
     "https://maps.app.goo.gl/2xStVoXpp77UcUZeA", False, "2025/11/cabadbaran_branch-1-scaled.png"),
]

# ---------------------------------------------------------------- Banner photos
HERO = [
    ("2025/11/front-page-2.png", "SOEMCO"),
    ("2025/10/loans_cover.png", "Loans"),
    ("2025/09/1739280853080-1-scaled-e1756976999800.jpg", "Savings Deposit"),
    ("2025/09/476923727_650083421021450_4039255247285347736_n.jpg", "Children and Youth Laboratory Cooperative"),
    ("2025/09/SOCORRO06-scaled-e1757314687496.jpg", "Life and Non-Life Insurance"),
    ("2025/09/FISHERY1-scaled-e1757315485736.jpg", "Allied Services"),
]

# ---------------------------------------------------------------- Products & services
# Category → programs → offerings (name, description, eligibility, image)
# Descriptions: blank line = new paragraph, lines starting with "- " = bullet list.
SERVICES = [
    {
        "slug": "loans", "name": "Loans", "icon": "💰", "image": "2025/10/loans_cover.png",
        "summary": "Funds that give you the power to act today, with a promise to pay back tomorrow.",
        "programs": [
            {
                "slug": "agricultural-loans", "name": "Agricultural Loans", "loan_type": "Agricultural",
                "image": "2025/11/agricultural_loan_profile-1024x683.png",
                "summary": "Affordable financing designed to help farmers and agri-entrepreneurs expand production, improve technology, and sustain livelihood through accessible capital assistance.",
                "offerings": [
                    ("MAPS-Fisherfolks Loan", "For financing and additional capital of small and medium fishing industry development including aqua culture.",
                     "Regular Members engaged in fishing and aqua culture production.", "2025/10/fisherfolk.png"),
                    ("MAPS-Livestock and Poultry Production Loan", "For financing and additional capital of livestock and poultry production.",
                     "Regular members engaged in poultry, hog raising, goat raising, and other forms of animal husbandry.", "2025/10/livestock_poultry.png"),
                    ("MAPS-Crop Production Loan", "For financing and additional working capital in farming and all forms of agricultural production activities.",
                     "Regular members engaged in farming and in all forms of agricultural production activities.", "2025/10/crops_production.png"),
                ],
            },
            {
                "slug": "business-loan", "name": "Business Loan", "loan_type": "Business",
                "image": "2025/09/business_loan_cover-1024x683.png",
                "summary": "Providing accessible financing to help our cooperative members grow their businesses, expand opportunities, and achieve sustainable success.",
                "offerings": [
                    ("BUKAS MSME-1", "Additional working capital.",
                     "Regular Members engaged in Micro, Small and Medium Enterprises (MSMEs) with minimum asset size of ₱30,000 and at least 6 months of existence.", ""),
                    ("BUKAS MSME-2", "Additional working capital.",
                     "Regular Members engaged in Micro, Small and Medium Enterprises (MSMEs) with minimum asset size of ₱100,000 and at least 1 year of existence.", ""),
                    ("BUKAS PLITE", "Additional working capital for barter and trading activities.",
                     "Regular Members engaged in barter and trading (ambulant vendors, small-time caterers/providers, etc.).", ""),
                    ("Asenso Credit Line", "A standby working capital intended for project-based business and contracting services, offered as a credit line facility. A borrower can draw down based on the available balance of the credit line on a designated fixed amount. The total credit line is considered a single account, so multiple drawdowns from a single credit line are not considered multiple accounts.",
                     "Regular Members engaged in project-based business (contractors/sub-contractors among others).", ""),
                    ("Asenso Business Loan", "Additional working capital; expansion of business and asset acquisition.",
                     "Regular Members engaged in Small, Medium and Large enterprises with asset size of ₱500,000 – ₱5M.", ""),
                    ("Asenso PLITE", "Additional working capital; expansion of business and asset acquisition, including fishing ventures (deep sea fishing).",
                     "Regular Members engaged in Small, Medium and Large enterprises with asset size of ₱500,000 – ₱1M.", ""),
                ],
            },
            {
                "slug": "personal-loan", "name": "Personal Loan", "loan_type": "Personal",
                "image": "2025/08/personal_loan_profile.png",
                "summary": "A convenient loan program designed to support your personal needs — from education and healthcare to household improvements and other essential expenses.",
                "offerings": [
                    ("Salary Loan – Government (Flat Interest)", "A personal loan for government-employed individuals.",
                     "Regular Members who are government employees with regular status; elected officials and co-terminus appointees (barangays and LGUs).", ""),
                    ("Salary Loan – Government (Diminishing Interest with Flat Amortization)", "A personal loan for government-employed individuals.",
                     "Regular Members who are government employees with regular status.", ""),
                    ("Salary Loan – Private", "A personal loan for privately employed individuals.",
                     "Regular Members who are private employees with regular status.", ""),
                    ("Salary Loan – Pension", "Financial assistance, medication and other future needs of pensioners.",
                     "Regular Members – Pension.", ""),
                ],
            },
            {
                "slug": "special-loans", "name": "Special Loans", "loan_type": "Special",
                "image": "2025/08/special_loan_profile-1024x683.png",
                "summary": "Flexible and fast-access loan options such as petty cash, instant, emergency, construction materials, and bonus loans — designed to support members in urgent and essential financial needs.",
                "offerings": [
                    ("Petty Cash Loan", "Intended for eventual and dire needs that require immediate financial assistance (Personal).",
                     "Regular Members who are employees with regular status; elected officials and co-terminus appointees (barangays and LGUs).", ""),
                    ("Instant Loan", "Loan against savings deposit.", "Regular Members in Good Standing.", ""),
                    ("Emergency Loan", "Immediate financial assistance in the event of hospitalization and death of the member and immediate family, including force majeure.", "", ""),
                    ("Construction Materials Loan", "To finance minor house repair and improvement.",
                     "Regular Members in Good Standing with owned house and lot.", ""),
                    ("Bonus Loan", "A form of cash advance against mid-year and year-end bonuses (Personal).",
                     "Members in Good Standing who are employed in either the government or private sector with regular status of employment.", ""),
                ],
            },
        ],
    },
    {
        "slug": "savings-deposit", "name": "Savings Deposit", "icon": "🏦",
        "image": "2025/09/1739280853080-1-scaled-e1756976999800.jpg",
        "summary": "Your money rests safely, while quietly earning interest.",
        "programs": [
            {
                "slug": "aflatoun-aflateen-savings", "name": "Aflatoun/Aflateen Savings",
                "image": "2025/10/savings_deposit-scaled.png",
                "summary": "A special savings program designed for children and teens to develop financial discipline, encourage responsibility, and build a secure future from an early age.",
                "offerings": [
                    ("Aflatoun/Aflateen Savings", "Let the children learn the habit of savings at a young age.",
                     "All Aflatoun/Aflateen Members.", ""),
                ],
            },
            {
                "slug": "gadget-travel-savings", "name": "Gadget & Travel Savings",
                "image": "2025/08/gadget_and_travel_savings.png",
                "summary": "A goal-oriented savings program that helps members prepare funds for the latest gadgets or dream travel experiences — making big purchases and adventures lighter and more achievable.",
                "offerings": [
                    ("Gadget Savings", "For purchase of gadgets and other technological products.", "Regular Members.", ""),
                    ("Travel Savings", "For vacation and travel purposes.", "", ""),
                ],
            },
            {
                "slug": "holiday-savings", "name": "Holiday Savings",
                "image": "2025/08/holiday_savings.png",
                "summary": "A disciplined savings plan designed to help members prepare for the holiday season — making gift-giving, celebrations, and family needs more affordable and worry-free.",
                "offerings": [
                    ("Birthday Savings", "For birthday celebration expenses.", "All members.", ""),
                    ("Wedding Savings", "For wedding expenses.", "", ""),
                    ("Christmas Savings", "For Christmas expenses.", "", ""),
                    ("Fiesta Savings", "For expenses during fiestas.", "", ""),
                    ("Graduation Savings", "For expenses during graduation.", "Regular Members with graduating children.", ""),
                ],
            },
            {
                "slug": "pension-savings", "name": "Pension Savings",
                "image": "2025/08/pension_loan_hero.png",
                "summary": "A long-term savings plan designed to help members prepare for retirement — ensuring financial security, stability, and peace of mind in the years ahead.",
                "offerings": [
                    ("Pension Savings Plan", "Financial security in retirement.", "Open to members aged 30 to 50 years old.", ""),
                ],
            },
            {
                "slug": "personal-access-savings", "name": "Personal Access Savings",
                "image": "2025/08/personal_access_savings.png",
                "summary": "A flexible savings program that allows members to securely save while maintaining easy access to funds whenever needed — combining safety with convenience.",
                "offerings": [
                    ("Personal Access Savings Account (PASA)", "Liquid savings account with no contractual maturity.", "All members.", ""),
                ],
            },
            {
                "slug": "time-deposit", "name": "Time Deposit",
                "image": "2025/08/time_deposit_savings.png",
                "summary": "Grow your money with guaranteed returns through fixed-term deposits — a safe and reliable way to maximize your savings while securing your financial future.",
                "offerings": [
                    ("Time Deposit", "Long-term savings.", "Regular Members.", ""),
                    ("Special Time Deposit", "Long-term savings with monthly payback on interest.", "", ""),
                ],
            },
        ],
    },
    {
        "slug": "children-and-youth-laboratory-coop", "name": "Children & Youth Laboratory Coop", "icon": "🌱",
        "image": "2025/09/476923727_650083421021450_4039255247285347736_n.jpg",
        "summary": "Social and financial education for children and youth aged 17 years and below.",
        "programs": [],
        "related": "aflatoun-aflateen-savings",
    },
    {
        "slug": "life-and-non-life-insurance", "name": "Life & Non-Life Insurance", "icon": "🛡️",
        "image": "2025/09/SOCORRO06-scaled-e1757314687496.jpg",
        "summary": "Protects you and your loved ones from financial loss due to an unexpected event.",
        "programs": [
            {
                "slug": "personal-accident-insurance", "name": "Personal Accident Insurance (Individual/Group)",
                "image": "2025/09/personal_accident_insurance.png",
                "summary": "To protect your loved ones, to leave an inheritance, to pay off debts and other expenses, to add more financial security, to give you peace of mind, and to mitigate risk.",
                "offerings": [
                    ("Coop AKSI (Individual)",
                     "The plan offers 24 hours a day, 365 days a year, worldwide protection against accidents an insured person may be exposed to in activities related to business or pleasure, whether on or off the job, at home or while travelling. Coverage includes, but is not restricted to, flying as a passenger (not as crew) on any commercial airline, on any regular, non-scheduled or chartered flight, or any military transport operated by a government authority.", "", ""),
                    ("Keyman Insurance (Individual)",
                     "Protection against accidents an insured person may be exposed to in activities related to business or pleasure, whether on or off the job, at home or while travelling. Coverage includes, but is not restricted to, flying as a passenger (not as crew) on any commercial airline, on any regular, non-scheduled or chartered flight, or any military transport operated by a government authority.",
                     "Individuals under Occupational Class 1 – strictly non-hazardous, white-collar occupations, e.g. clerks, secretaries, doctors, dentists, executives, teachers, co-op leaders, managers and supervisors.", ""),
                    ("Travel Personal Accident Insurance (Individual)",
                     "Covers death and dismemberment from bodily injuries caused by accident. It pays the full principal sum for accidental death, or loss of limbs, eyes, hands, or all fingers and both thumbs, and half of the principal sum for accidental loss of one hand, one foot or sight of one eye. Losses must occur within 180 days after the accident.", "", ""),
                    ("CLIMBS Health & Accident Insurance (Individual)",
                     "Protection for members/policyholders against loss of income as a result of death due to accident, and when they become hospitalized due to natural illness or accident.", "", ""),
                    ("PATXT15 (Individual)", "Affordable personal accident protection for everyone. Insurance protection at your fingertips!", "", ""),
                    ("Student Personal Accident Insurance (Group)", "Group term accident insurance coverage designed for students.", "", ""),
                    ("MARINA PA (Group)",
                     "If a passenger survives and is recovered from the sinking wreckage of the vessel, CLIMBS will immediately reimburse the survivor's expenses up to ₱50,000 for daily meals, transportation and clothing until the passenger reaches their destination or returns safely home.\n\nIn the event of a covered death, CLIMBS will reimburse expenses incurred to transport the mortal remains back to the passenger's residence anywhere in the Philippines, up to ₱20,000 per passenger.", "", ""),
                    ("CLIMBS Security Enforcer Insurance (Group)",
                     "Financial protection for security enforcers aged 18–60, covering risks arising from accidents and work-related incidents. Coverage includes accidental death and dismemberment, accident medical expense reimbursement, burial assistance (due to accident or sickness), and unprovoked murder or assault, with two benefit options. Enrollment requires a master list of at least 25 persons and is covered on an annual premium basis.", "", ""),
                    ("Family Medical Insurance (Group)",
                     "- Yearly renewable insurance with one (1) year coverage\n- No medical examination required\n- Exclusive to coop members and employees\n- Minimum of 1,000 enrollees\n\nCovers in-patient hospitalization expenses of the insured in excess of PhilHealth and other HMO benefits, up to the maximum coverage; out-patient expenses are not covered. Benefits cover actual out-of-pocket expenses for room and board, surgical, physician, laboratory, medicines and other expenses necessary for treatment. Prescribed medicines bought outside are covered if bought during the confinement period. The plan is non-convertible to cash.", "", ""),
                    ("Motor Car Insurance",
                     "Compulsory Third Party Liability (CTPL). Note: a CTPL policy does not cover loss or damage to third-party property.\n\nComprehensive motor car insurance covers:\n- Own damage / theft\n- Third-party bodily injury\n- Third-party property damage\n- Auto PA (optional)\n- Acts of nature (optional)", "", ""),
                    ("Standard Fire Insurance",
                     "Financial protection for residential properties against loss or damage caused by fire and related risks, helping homeowners recover and rebuild after unforeseen disasters.\n\n- Standard coverage (without Allied Perils): protects against fire and lightning\n- Expanded coverage (with Allied Perils): adds earthquake fire and shock, typhoon, flood, explosion and riot\n\nStandard Fire Insurance safeguards your home, supports loan obligations, and gives peace of mind when disasters strike.", "", ""),
                ],
            },
        ],
    },
    {
        "slug": "allied-services", "name": "Allied Services", "icon": "🤝",
        "image": "2025/09/FISHERY1-scaled-e1757315485736.jpg",
        "summary": "Supporting services to enhance the economic, social, and livelihood opportunities of its members and community.",
        "programs": [
            {
                "slug": "convenience-store-and-pharmacy", "name": "Convenience Store and Pharmacy",
                "image": "2025/10/store-1024x683.png", "photo2": "2025/10/store_group_picture-scaled.png",
                "people": "Supervisor: Diana B. Dano",
                "summary": "Providing convenient, one-stop access to pharmaceuticals and daily essentials, helping our community save time, manage their health, and experience true convenience.",
                "offerings": [],
            },
            {
                "slug": "hardware", "name": "Hardware",
                "image": "2025/10/hardware-1024x683.png", "photo2": "2025/10/hardware_group_picture-scaled.png",
                "people": "Supervisor: Weldelito C. Ramirez",
                "summary": "All the physical tools, materials and fixtures — like fasteners, plumbing and electrical supplies — essential for construction, repair and maintenance projects.",
                "offerings": [],
            },
            {
                "slug": "mv-mariner", "name": "MV Mariner",
                "image": "2025/10/mariner_cover-1024x683.png", "photo2": "2025/10/mariner_1.jpg",
                "people": "Boat Captains: Ramil M. Dumalag and Randy Estrella",
                "summary": "A modern fast craft — a high-speed passenger vessel engineered to reduce inter-island travel time by prioritizing speed and efficiency over cargo capacity.",
                "offerings": [],
            },
        ],
    },
    {
        "slug": "todo-benepisyo", "name": "TODO Benepisyo", "icon": "🆘", "image": "",
        "summary": "Quick funds for crises like disasters or family emergencies, ensuring swift relief.",
        "programs": [],
    },
]

# ---------------------------------------------------------------- Member stories (original Cebuano text)
STORIES = [
    ("Sonia’s Story", "Sonia B. Estrella", "Regional Outstanding Rural Woman 2022, Department of Agriculture-Caraga", "Socorro Branch",
     "2025/11/SOCORRO11-1024x576.jpg",
     "Tungod sa SOEMCO, natabangan gajud ang ahung pag-panguma sa gihatag tungod niini hing-imporve ang ahung pag-panguma.\n\n"
     "Og dugang pa, gisaligan ko nila nga maka-utang og tunga sa milyon aron capital sa ahong tindahan, mao nga nakapalit ko ug lote nga maoy among gitukoran og tindahan.\n\n"
     "Salamat sa suporta sa SOEMCO nga nakapadajun mi sa among pagpanguma og napalambo namo ang among pagnegosyo, Karon, naa nako'y Sonia Small Family Farm sa Brgy. Estrella, og tungod niini nakita sa Department of Agriculture ang ahong pagpaningkamot, og nahimo kong awardee pinaagi sa ahung pagpananom."),
    ("Delia’s Story", "Delia Bayogbog", "Kitcharao, Agusan del Norte", "Alegria Branch",
     "2025/11/alegria-1024x576.jpg",
     "Dugay nako nga membro sa SOEMCO. Since 2000, an ako negosyo gyud kay bakery og naplete pa ko adto og 500 per month. Nagstart ang SOEMCO sa Alegria year 2012, og ang area nga akong gipletehan ibaligya, nitry ko og dool sa SOEMCO og the best gyud ang SOEMCO kay ila kong gitabangan. Karon, naa nako'y building og naa nako'y restaurant tapad sa kong bakery. Tungod sa SOEMCO, nakapalit ko'g car, nakapundar nako og up and down nga balay og naa nasad ko'y dahang mga tawo nga nitabang sa negosyo.\n\n"
     "Og dili tungod sa SOEMCO Alegria Branch, dili pod ko maingun-ani. Wala ko'y laing bangko nga gi-utangan, SOEMCO ra gyud. Daghang salamat SOEMCO."),
    ("Roel’s Story", "Roel Jeremy Diaz", "Brgy. Magosilom, Cantilan, Surigao del Sur", "Cantilan Branch",
     "2025/11/cantilan-1024x576.jpg",
     "It was my dream to have a business after my retirement para may icome pa ako, sa ako tambay and basic needs. When i started the poultry business, inato lang. In fact, walay pangalan ang negosyo. But as the time goes by, I needed capitalization for the expansion.\n\n"
     "So, I went to other private banks pero hamok nga requirements. I remember SOEMCO because i have some frieds working there, Nathan and Kevin. They readily offer to me a loan for the expansion of my business. Dako an nahitabang nan SOEMCO sa capitalization sa ako business.\n\n"
     "If you're really serious with your business plan ventures pero naproblema sa capital, I would recommend mag inquire sa SOEMCO, an SOEMCO ang fastest way mag approve nan (loan) application and interest rate is kaya naman. An mga personnel paspas mu-entertain para maguide sa business plan."),
    ("Gegie’s Story", "Gegie Montano", "Brgy. Luna, Surigao City", "Surigao Branch, member since 2016",
     "2025/11/surigao-1024x576.jpg",
     "Ganahan ko sa SOEMCO kay wala'y duha-duha nga gi-grant ang akong loan para sa negosyo nga fruitstand. Daghang benefits sa mga members labi na pareho nako nga single mom. Tungod sa SOEMCO. nakapa-eskwela ko sa akong mga anak, ang tulo nahuman na, nakapalit ko'g sakyanan napalago akong negosyo og nakatabang pa ko sa uban."),
    ("Arenza’s Story", "Roel Arenza", "Brgy. 2, Dapa, Siargao", "Dapa Branch",
     "2025/11/dapa-1024x576.jpg",
     "Gikan sa negosyong gamay nga sapatosan, nagsugod og angat ahong ukay-ukayan sa dihang na-membro ko sa SOEMCO pinaagi ni Kevin Tesado. Maayo na ang kahimtang sa akong negosyo nga na-membero ko sa SOEMCO. Dako kaayo ko og pasalamat sa SOEMCO. Labi na sa mga benepisyo matag Disyembre nga akong madawat."),
    ("Reynaldo & Denise’s Story", "Reynaldo Badillo and Denise May Badillo", "SOEMCO Member for 6 years", "Claver Branch",
     "2025/11/claver-1024x576.jpg",
     "Ang among business is printing and sublimation nagsugod sa 2011. Sauna nagrenta pa mi, pero just last year nakatukod mi sa among building tungod sa SOEMCO.\n\n"
     "Sa wala pa ang SOEMCO, wala'y capital kay dinagko ang volume sa orders, ang akong amiga nga si Sassy nagdala sa ako sa SOEMCO. Dali kaayo doolon and accomodating ang mga personnel. Affordable interest rates sa loan, libre ang plete and accomodation panahon sa General Assembly.\n\n"
     "Nindot ang SOEMCO, pa-membro na!"),
]

# ---------------------------------------------------------------- FAQs
FAQS = [
    ("Who can join?", "Anyone qualified can become a member — Filipino citizens only."),
    ("Requirements for membership?",
     "- Membership Application Form & Signature Card\n- 2 pcs. 1x1 ID picture\n- Copies of at least 2 valid IDs with 3 signatures\n- Photocopy of Birth or Marriage Certificate"),
    ("Requirements for loans?",
     "- Loan Application Form\n- Photocopy of CEDULA\n- Copies of at least 2 valid IDs with 3 signatures (Maker)\n- Photocopy of at least 1 valid ID with 3 signatures (Co-Maker)"),
    ("How do I apply?", "Visit our office, submit the requirements, and fill out a form. You can also start your application online and a SOEMCO officer will contact you."),
    ("How long will the processing take?", "2 to 3 days."),
    ("What loans are available?", "Personal, business, emergency, agricultural, and special loans."),
    ("How much can I borrow?", "It depends on your savings, share capital, and capacity to pay."),
    ("Are loan interest rates high?", "No. Rates are fair, member-friendly, and lower than most private lenders."),
    ("Can I earn interest on my savings with SOEMCO?",
     "Yes — SOEMCO savings deposits earn interest. See Savings Deposit for the available plans, and ask your branch for current rates."),
    ("Does SOEMCO offer livelihood training or programs?", "Yes."),
    ("Why choose our cooperative?", "Safe. Trusted. Member-owned. Community-centered."),
]

# ---------------------------------------------------------------- Downloadable forms
FORMS = [
    # title, category, description, file path
    ("Membership Application Form", "Membership", "For new members. Submit with your IDs and photos.", "2026/05/MEMBERSHIP-APPLICATION-FORM-2-1.docx"),
    ("Signature Card", "Membership", "Specimen signature card for new members.", "2026/05/SIGNATURE-CARD-1-1.pdf"),
    ("Loan Application Form", "Loan documents", "Required for all loan applications.", "2025/12/New-Loan-Application.docx"),
    ("Co-Maker’s Statement", "Loan documents", "To be filled out by your co-maker.", "2025/12/Co-Makers-Statement.docx"),
    ("Promissory Note", "Loan documents", "Signed when your loan is released.", "2025/12/Promissory-Note.docx"),
    ("Acknowledgement", "Loan documents", "Acknowledgement form for loan documents.", "2025/12/Acknowledgement.docx"),
    ("Special Power of Attorney (SPA)", "Loan documents", "Barangay SPA form.", "2025/12/Special-Power-Of-Attorney-SPA-Barangay.docx"),
]

# ---------------------------------------------------------------- Announcements (shown on the home page while active)
ANNOUNCEMENTS = [
    ("30th SOEMCO Annual General Assembly",
     "ALANG SA TANANG MEMBRO SA SOEMCO! Gidapit ang tanang membro sa Ika-30th Tinuig nga Asembleya Heneral sa SOEMCO sa Marso 28, 2026 (Sabado) sa Socorro Municipal Gymnasium, Socorro, Surigao del Norte.\n\n"
     "Adunay meal allowance nga PhP 150.00 alang sa paniudto (cash para sa Socorro Branch ug packed lunch para sa ubang branches). Ang makaapil sa pagbotar, raffle draw, ug giveaways mao lamang ang Members in Good Standing (MIGS) kutob sa Pebrero 28, 2026, ug kinahanglan adunay CBU nga PhP 2,000.00 pataas ug personal nga motambong.\n\n"
     "Ang deadline sa pagsumite sa Certificate of Candidacy kay Marso 6, 2026, alas 5:00 sa hapon ngadto sa Election Committee, ug ang cut-off sa pag-claim sa raffle tickets ug giveaways kutob ra sa ala-1:00 sa hapon sa adlaw sa asembliya.",
     False),  # the assembly has passed, so this starts hidden; tick "active" in /admin/ to show an announcement
]

# ---------------------------------------------------------------- News
NEWS = [
    {
        "slug": "soemco-joins-the-68th-araw-ng-socorro-celebration", "date": date(2026, 2, 25), "tag": "Community",
        "title": "SOEMCO Joins the 68th Araw ng Socorro Celebration, Showcasing Support at Harog “Benignit” Festival",
        "images": ["2026/02/641318038_1502668231860141_7821961223721443047_n.jpg"],
        "body": [
            "Socorro, Surigao del Norte — In vibrant colors, rich tradition, and strong community spirit, SOEMCO once again took part in the annual Harog “Benignit” Festival in celebration of the 68th Araw ng Socorro held on February 22, 2026.",
            "The Harog “Benignit” Festival, one of the most anticipated highlights of Araw ng Socorro, showcases the municipality’s cultural heritage through the preparation and sharing of Benignit—a beloved Filipino delicacy made from coconut milk, root crops, bananas, and sago pearls. Traditionally, Harog (Benignit) is prepared as a comforting delicacy or snack served after the tiring Hinabangay which is not just means communal work, yet Bayanihan means helping each other during calamities, when there is a house to be transferred and building one rendering work for free, when death comes to a family, and in other instances where there is a need for collective help symbolizing care, gratitude, and the Bayanihan spirit among community members.",
            "As a long-time partner of the local government and the community, SOEMCO actively participated in the festivities, demonstrating its continued commitment to supporting cultural preservation and local development. Through its presence and engagement, the cooperative reaffirmed its role not only as a financial institution but also as a community partner that celebrates and uplifts local traditions.",
            "The 68th Araw ng Socorro celebration gathered residents, local officials, organizations, and visitors in a day filled with cultural presentations, thanksgiving activities, and festive gatherings. The event served as a reminder of Socorro’s growth over the years and the collective efforts of its people in shaping a progressive and resilient municipality.",
            "SOEMCO’s participation highlights its dedication to being deeply rooted in the community it serves. By supporting events such as the Harog “Benignit” Festival, the cooperative strengthens its bond with members and stakeholders while honoring the rich cultural identity of Socorro.",
            "As Socorro marks 68 years of progress and unity, SOEMCO stands proud to celebrate alongside the community continuing its mission of service, solidarity, and shared prosperity.",
        ],
    },
    {
        "slug": "soemco-and-soces-seal-partnership-aflatoun-savings", "date": date(2026, 2, 25), "tag": "Community",
        "title": "SOEMCO and SOCES Seal Partnership Through MOA Signing on Aflatoun Savings Program, Coupled with Heartwarming Gift-Giving Activity",
        "images": ["2026/02/597774872_898788049484318_4702850374116583535_n.jpg", "2026/02/597607356_898788126150977_5471639882181597506_n.jpg",
                   "2026/02/600248825_898788236150966_4868511228053789048_n.jpg", "2026/02/597698850_898787962817660_5509061404001591827_n.jpg",
                   "2026/02/599386704_898787956150994_7745986934966949034_n.jpg"],
        "body": [
            "Socorro, Surigao del Norte — On December 16, 2025, a significant milestone in advancing financial education among young learners was achieved as a Memorandum of Agreement (MOA) was officially signed between SOEMCO and Socorro Central Elementary School (SOCES) for the implementation of the Aflatoun Savings Program. The partnership reflects a shared commitment to strengthening financial literacy, values formation, and social responsibility among pupils through structured and meaningful learning initiatives.",
            "The Aflatoun Savings Program is a globally recognized educational initiative that equips children and youth with essential knowledge on saving, budgeting, and responsible decision-making. By integrating financial education with social awareness, the program aims to nurture disciplined, confident, and socially responsible individuals who are prepared to make wise financial choices for a more secure future.",
            "During the ceremony, school officials, cooperative representatives, and pupils gathered to witness the formalization of the partnership, marking a collaborative effort to promote a culture of saving and financial awareness within the school community. The MOA signing symbolizes a long-term commitment to empowering learners with practical life skills that extend beyond the classroom and into their daily lives.",
            "Adding warmth and joy to the event, a gift-giving activity was also conducted, bringing smiles and excitement to the pupils as they received presents in celebration of the Christmas season. The initiative highlighted not only the importance of financial education but also the spirit of generosity, compassion, and community service. Laughter and gratitude filled the venue, creating a festive and meaningful atmosphere for everyone present.",
            "School representatives expressed their appreciation for the partnership, emphasizing how programs like Aflatoun help shape responsible and future-ready learners. Meanwhile, SOEMCO reaffirmed its mission of extending care and impactful programs to schools and communities, especially in nurturing the financial and social development of the youth.",
            "Through this collaborative effort, SOEMCO and SOCES continue to champion education that empowers children to save, grow, and thrive. The successful MOA signing and gift-giving activity stand as a testament to the power of partnership in building financially literate, value-driven, and socially conscious young individuals.",
        ],
    },
    {
        "slug": "financial-literacy-aflatoun-orientation-del-carmen", "date": date(2026, 2, 25), "tag": "Outreach",
        "title": "SOEMCO Brings Financial Literacy & Aflatoun Savings Orientation to Remote Communities in Del Carmen, SDN",
        "images": ["2026/02/573893457_860548349974955_9034905236583378165_n.jpg", "2026/02/572035271_860549053308218_2485039410194491904_n-768x1024.jpg",
                   "2026/02/571193633_860549276641529_9012804249530915075_n-1024x768.jpg", "2026/02/574861420_860548536641603_5420176141271254849_n-768x1024.jpg",
                   "2026/02/572221868_860549209974869_3634163784714315480_n-1024x768.jpg"],
        "body": [
            "On October 28, 2025, a meaningful step toward financial empowerment was successfully realized as a Financial Literacy and Aflatoun Savings Orientation was conducted in Sitio Sugba and Sitio Liaonan, Barangay Caub, Del Carmen, Surigao del Norte. The activity was carried out in partnership with the Espoir School of Life through the Aflatoun Savings Program, highlighting a shared commitment to nurturing financially responsible and future-ready learners and community members.",
            "The orientation gathered young learners, parents, and local residents in an engaging and educational session focused on the importance of saving, smart spending, and financial discipline. Through interactive discussions and practical examples, participants were introduced to basic financial concepts such as budgeting, goal setting, and the value of consistent saving — essential life skills that contribute to long-term personal and community development.",
            "The Aflatoun Savings Program, known for promoting social and financial education among children and youth, played a key role in the initiative by providing a learner-centered approach that encourages responsibility, confidence, and economic awareness at an early age. With the guidance of facilitators, learners were inspired to develop positive financial habits and understand how small savings today can lead to greater opportunities in the future.",
            "Despite the geographical challenges of reaching remote areas, SOEMCO remained steadfast in its mission to deliver inclusive and accessible services. The successful conduct of the orientation in Sitio Sugba and Sitio Liaonan reflects the cooperative’s unwavering dedication to extending financial education to underserved communities, ensuring that no one is left behind in the journey toward financial literacy.",
            "Community leaders and residents expressed their appreciation for the initiative, emphasizing how such programs empower families to make informed financial decisions and build a more secure future. The activity also strengthened community ties, reinforcing the importance of collaboration between educational institutions, cooperatives, and local stakeholders in promoting sustainable development.",
            "True to its commitment of providing “care within your reach,” SOEMCO continues to expand its outreach efforts by bringing impactful programs directly to grassroots communities. This initiative not only promotes financial awareness but also fosters a culture of saving, resilience, and self-reliance among the youth and the wider community.",
            "With continued partnerships and sustained efforts, SOEMCO and Espoir School of Life reaffirm their dedication to shaping financially literate individuals who are capable of growing, thriving, and contributing positively to their communities — proving that meaningful change begins with education, empowerment, and access, even in the most remote areas. 💙💛",
        ],
    },
    {
        "slug": "spider-and-organizational-capacity-assessment", "date": date(2025, 7, 28), "tag": "Community",
        "title": "Strengthening Partners on Development through Empowerment and Reflections (SPIDER) and Organizational Capacity Assessment (OCA)",
        "images": ["2025/07/518379924_10229709242651683_4711080303663337254_n.jpg"],
        "body": [
            "Socorro Empowered People’s Cooperative (SOEMCO) successfully conducted a 1.5-day Strengthening Partners on Development through Empowerment and Reflections (SPIDER) and Organizational Capacity Assessment (OCA) on July 18–19, 2025, at the SOEMCO Function Hall in Socorro, Surigao del Norte, Philippines.",
            "The activity was facilitated by representatives from the AgriCOOPh Federation and the Belgium-based NGO Trias Southeast Asia, bringing together SOEMCO officers, management, members, and Children and Youth Laboratory Cooperative officers. The sessions focused on deepening understanding of cooperative principles, strengthening leadership and governance, and assessing organizational systems and capacities.",
            "The SPIDER and OCA activities provided a meaningful venue for reflection, learning, and empowerment, enabling participants to identify strengths, areas for improvement, and strategic directions for sustainable growth. The assessment also reinforced collaboration among stakeholders and partners in development.",
            "SOEMCO expresses gratitude to God for the gift of wisdom, passion, and endurance granted to all participants, as well as to its partners for their guidance and support. Through initiatives like these, SOEMCO continues to strengthen its organization and advance its mission of empowering members and communities.",
        ],
    },
    {
        "slug": "fire-safety-seminar-and-fire-drill", "date": date(2025, 4, 25), "tag": "Community",
        "title": "SOEMCO Participates in the Fire Safety Seminar and Fire Drill",
        "images": ["2025/04/soemco-participates-in-the-fire-safety-seminar-and-fire-drill-thumbnail.jpg"],
        "body": [
            "Socorro Empowered People’s Cooperative (SOEMCO) actively participated in a Fire Safety Seminar and Fire Drill aimed at strengthening preparedness and ensuring the safety of its officers and employees.",
            "The activity provided participants with essential knowledge on fire prevention, proper use of fire extinguishers, emergency response procedures, and evacuation protocols during fire-related incidents. Through the hands-on fire drill, SOEMCO personnel were able to apply what they learned in a simulated emergency scenario, enhancing their awareness, coordination, and readiness.",
            "SOEMCO’s participation reflects its strong commitment to workplace safety, disaster preparedness, and the well-being of its members and employees. By continuously engaging in safety trainings and drills, the cooperative ensures that everyone is equipped with the skills and confidence needed to respond effectively during emergencies.",
            "The activity also strengthened collaboration between SOEMCO and partner agencies, promoting a culture of safety and preparedness within the organization and the wider community.",
            "SOEMCO remains dedicated to fostering a safe and resilient working environment for all.",
        ],
    },
    {
        "slug": "coastal-cleanup-and-tree-planting", "date": date(2025, 4, 25), "tag": "Environment",
        "title": "SOEMCO Employees Joined Coastal Cleanup & Tree Planting",
        "images": ["2025/04/soemco-employees-joined-coastal-cleanup-amptree-planting-thumbnail.jpg"],
        "body": [
            "Employees of the Socorro Empowered People’s Cooperative (SOEMCO) actively participated in a Coastal Cleanup and Tree Planting activity, demonstrating the cooperative’s strong commitment to environmental protection and community responsibility.",
            "The activity aimed to promote environmental awareness, reduce coastal waste, and help restore natural ecosystems through tree planting. SOEMCO employees worked hand in hand in collecting trash along the shoreline and planting trees, contributing to a cleaner environment and a more sustainable future.",
            "Through this initiative, SOEMCO reinforced the importance of collective action in caring for the environment while encouraging employees to be responsible stewards of nature. The activity also fostered teamwork, unity, and a shared sense of purpose among participants.",
            "SOEMCO continues to support environmental programs that protect natural resources and promote sustainable development for the benefit of present and future generations.",
        ],
    },
    {
        "slug": "spreading-love-and-joy-this-christmas-season", "date": date(2025, 4, 25), "tag": "Community",
        "title": "Spreading Love and Joy this Christmas Season",
        "images": ["2025/04/spreading-love-joy-christmas-thumbnail.jpg"],
        "body": [
            "This Christmas, the Socorro Empowered People’s Cooperative (SOEMCO) once again lit up the season with warmth, hope, and generosity, spreading love and joy to its members, employees, and the community. True to the spirit of Christmas, SOEMCO’s celebrations emphasized compassion, unity, and the joy of giving.",
            "Through a series of outreach programs, gift-giving initiatives, and festive activities, the cooperative reached out to families and children, bringing smiles and heartfelt cheer. Employees and members actively participated in preparing gifts, organizing events, and delivering tokens of goodwill, demonstrating that the power of sharing can brighten lives and strengthen community bonds.",
            "Beyond the festive celebrations, this initiative reflects SOEMCO’s enduring commitment to uplifting the community, fostering solidarity, and creating meaningful connections. By celebrating together and giving back, the cooperative reinforces its vision of building a caring, supportive, and joyful community for all.",
        ],
    },
    {
        "slug": "united-we-play-united-we-win", "date": date(2025, 4, 25), "tag": "Events",
        "title": "United We Play, United We Win: Stronger Together through Sportsmanship!",
        "images": ["2025/04/united-we-play-united-we-win-stronger-together-through-sportsmanship-thumbnail.jpg"],
        "body": [
            "The Socorro Empowered People’s Cooperative (SOEMCO) recently hosted an exciting and inspiring sports event under the theme “United We Play, United We Win: Stronger Together through Sportsmanship!” The activity brought together members, employees, and community partners for a day filled with friendly competition, teamwork, and fun.",
            "Participants engaged in a variety of sports and games, from basketball and volleyball to relay races and fun team challenges. Beyond showcasing athletic abilities, the event emphasized values of teamwork, cooperation, respect, and fair play, encouraging participants to work together toward common goals.",
            "The sports activity also served as a platform for building stronger relationships among members, employees, and the community. By fostering camaraderie and unity, SOEMCO reinforced its commitment to holistic development—promoting physical wellness, mental resilience, and social engagement.",
            "Through initiatives like this, SOEMCO demonstrates that growth is not only measured by financial success but also by the strength of the relationships and sense of community it nurtures. The cooperative believes that when people come together in play, they cultivate a spirit of collaboration and shared pride that extends beyond the playing field.",
            "The event concluded with recognition of outstanding teams and players, highlighting both skill and sportsmanship. SOEMCO’s message was clear: together, the cooperative and its members can achieve more, grow stronger, and build a more united and supportive community.",
        ],
    },
    {
        "slug": "stronger-together-today-for-a-brighter-tomorrow", "date": date(2025, 4, 25), "tag": "Events",
        "title": "Stronger Together Today for a Brighter Tomorrow!",
        "images": ["2025/04/stronger-together-today-for-a-brighter-tomorrow-thumbnail.jpg"],
        "body": [
            "The Socorro Empowered People’s Cooperative (SOEMCO) proudly celebrated Annual Cooperative Month with the theme “Stronger Together Today for a Brighter Tomorrow!”, highlighting the cooperative’s dedication to unity, collaboration, and sustainable growth.",
            "The celebration brought together officers, members, staff, and community partners in a series of activities that showcased the values of cooperation, teamwork, and mutual support. Participants engaged in educational seminars, team-building exercises, and fun community events that emphasized the role of cooperatives in fostering economic empowerment and social development.",
            "Through the month-long celebration, SOEMCO reinforced its commitment to building stronger partnerships, nurturing active membership, and promoting inclusive growth. The activities also served as a platform to recognize outstanding members and initiatives that exemplify the spirit of cooperation.",
            "By commemorating Cooperative Month, SOEMCO underscores its vision of creating a brighter and more resilient community—one that thrives on collaboration, shared responsibility, and the empowerment of every member.",
        ],
    },
    {
        "slug": "happy-13th-anniversary-soemco-claver", "date": date(2025, 4, 25), "tag": "Branches",
        "title": "Happy 13th Anniversary, SOEMCO Claver",
        "images": ["2025/04/happy-13th-anniversary-soemco-claver-thumbnail.jpg"],
        "body": [
            "The Socorro Empowered People’s Cooperative (SOEMCO) Claver Branch proudly celebrated its 13th Anniversary, marking thirteen years of committed service, steady growth, and dedication to empowering members and strengthening the community.",
            "The anniversary celebration brought together SOEMCO officers, management, staff, members, and partners in a meaningful gathering that reflected on the branch’s milestones and contributions to local development. The event highlighted the trust and support of members who have been instrumental in the continued success of the Claver Branch.",
            "For the past thirteen years, the SOEMCO Claver Branch has consistently provided accessible financial services, promoted savings and investments, and supported livelihood opportunities that have improved the lives of its members. The celebration also recognized the dedication and hard work of officers and staff who continue to uphold the cooperative’s core values.",
            "As it marks this milestone, SOEMCO Claver Branch reaffirms its commitment to service excellence, partnership, and community empowerment, looking forward to more years of growth and shared success.",
        ],
    },
    {
        "slug": "soemco-28th-annual-general-assembly", "date": date(2025, 4, 24), "tag": "Assembly",
        "title": "SOEMCO 28th Annual General Assembly",
        "images": ["2025/04/soemco-28th-annual-general-assembly-thumbnail.jpg"],
        "body": [
            "The Socorro Empowered People’s Cooperative (SOEMCO) successfully held its 28th Annual General Assembly, bringing together officers, members, management, and stakeholders in a significant gathering that highlighted unity, transparency, and shared progress.",
            "The assembly served as a platform to present the cooperative’s accomplishments, financial performance, and major initiatives over the past year. Members were also informed of plans and strategic directions aimed at sustaining growth, strengthening services, and further empowering communities.",
            "Key agenda items included reports from the Board of Directors and Management, discussions on cooperative programs, and the reaffirmation of SOEMCO’s commitment to good governance, accountability, and member participation. The active involvement of members reflected the cooperative’s strong democratic foundation.",
            "Through the 28th Annual General Assembly, SOEMCO reinforced its mission of service excellence and inclusive development, recognizing the vital role of its members in achieving the cooperative’s continued success.",
        ],
    },
    {
        "slug": "babae-ka-hindi-babae-lang", "date": date(2025, 4, 24), "tag": "Events",
        "title": "Babae Ka, Hindi Babae Lang",
        "images": ["2025/04/babae-ka-hinde-babae-lang-thumbnail.jpg"],
        "body": [
            "In celebration of Women’s Month 2024, the Socorro Empowered People’s Cooperative (SOEMCO) proudly joined the nationwide observance under the theme “Lipunang Patas sa Bagong Pilipinas: Kakayahan ng Kababaihan, Patunayan!” highlighting the strength, resilience, and vital role of women in building a just and progressive society.",
            "Anchored on the empowering message “Babae Ka, Hindi Babae Lang,” the celebration recognized women not only as nurturers but also as leaders, professionals, and changemakers within the cooperative and the community. Various activities were conducted to promote gender equality, women’s empowerment, and awareness of women’s rights and contributions.",
            "SOEMCO officers, employees, members, and women leaders actively participated in discussions, advocacies, and activities that emphasized women’s capabilities, leadership, and significant contributions to economic and social development. The celebration also served as a platform to inspire confidence, solidarity, and collective action among women.",
            "Through this observance, SOEMCO reaffirmed its commitment to promoting inclusive development, gender equality, and a workplace and community where women are empowered to lead, succeed, and thrive.",
        ],
    },
    {
        "slug": "grand-opening-parade-63rd-adlaw-sa-socorro", "date": date(2025, 4, 24), "tag": "Community",
        "title": "Grand Opening Parade & Declaration of the 63rd Adlaw sa Socorro",
        "images": ["2025/04/grand-opening-parade-declaration-of-the-63rd-adlaw-sa-socorro-thumbnail.jpg"],
        "body": [
            "The Municipality of Socorro officially kicked off the celebration of the 63rd Adlaw sa Socorro with a vibrant Grand Opening Parade and Declaration Ceremony, marking the start of a series of activities honoring the town’s history, culture, and unity.",
            "Colorful floats, lively street performances, and coordinated contingents from various sectors filled the streets of Socorro, showcasing the community’s rich heritage and festive spirit. The parade symbolized solidarity and pride among residents as they came together to celebrate another year of progress and shared identity.",
            "The declaration ceremony formally opened the festivities, highlighting the significance of the 63rd Adlaw sa Socorro as a tribute to the municipality’s journey, achievements, and aspirations for continued growth and development. Local officials, organizations, and community members participated in the event, expressing collective commitment to strengthening unity and cooperation.",
            "The Grand Opening Parade and Declaration set an energetic and meaningful tone for the celebration, reflecting Socorro’s enduring spirit, cultural pride, and strong sense of community as it commemorates its 63rd founding anniversary.",
        ],
    },
    {
        "slug": "world-cleanup-day", "date": date(2025, 4, 13), "tag": "Environment",
        "title": "SOEMCO Staff Proudly Participated in World Cleanup Day",
        "images": ["2025/04/post-featured-image-02.jpg"],
        "body": [
            "In a strong show of environmental stewardship, employees of the Socorro Empowered People’s Cooperative (SOEMCO) actively participated in a Coastal Cleanup and Tree Planting activity, reinforcing the cooperative’s commitment to a cleaner and greener community.",
            "The event focused on reducing coastal waste and restoring natural habitats through tree planting. SOEMCO employees collaborated in collecting trash along the shoreline and planting trees, contributing to the preservation of the environment and the promotion of sustainable development.",
            "Through this initiative, SOEMCO emphasized the importance of teamwork, responsibility, and active participation in environmental protection. The activity also encouraged community involvement, demonstrating that collective action can lead to a healthier and more sustainable environment.",
            "SOEMCO continues to lead by example, promoting programs that safeguard natural resources for the benefit of present and future generations.",
        ],
    },
    {
        "slug": "walang-gutom-program-dswd-partnership", "date": date(2025, 4, 13), "tag": "Outreach",
        "title": "Walang Gutom Program of DSWD in Partnership with SOEMCO",
        "images": ["2025/12/493177857_1235602065233427_5771872010228235287_n.jpg", "2025/12/494005002_1235602225233411_1719660884205243168_n-1024x683.jpg"],
        "body": [
            "The Socorro Empowered People’s Cooperative (SOEMCO) proudly partnered with the Department of Social Welfare and Development (DSWD) to implement the “Walang Gutom” Program, a government initiative aimed at providing nutritious meals to families in need.",
            "Through this partnership, SOEMCO helped ensure that parents, as primary beneficiaries, received regular, nutritious food packs, promoting the health and well-being of their households. By supporting families, the program indirectly benefits children, helping them thrive in a healthier and more nurturing environment.",
            "SOEMCO’s involvement highlights its commitment not only to financial empowerment but also to social responsibility and community welfare. By joining forces with DSWD, the cooperative contributes to stronger, healthier, and more resilient families in the community.",
            "The “Walang Gutom” Program reflects SOEMCO’s vision of supporting initiatives that uplift the lives of families, ensuring that no parent or child in the community goes hungry.",
        ],
    },
]

# Titles of the short placeholder items from the first version of this site; `seed` removes them.
OLD_PLACEHOLDER_NEWS = [
    "SOEMCO joins the 68th Araw ng Socorro",
    "SOEMCO and SOCES sign Aflatoun Savings MOA",
    "Financial literacy reaches Del Carmen's remote sitios",
]
