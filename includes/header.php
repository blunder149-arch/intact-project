<!-- Header Main Area -->
		<header class="site-header header-style-3">
			<div class="pbmit-pre-header-wrapper">
				<div class="container">
					<div class="d-flex justify-content-between">
						<div class="pbmit-pre-header-left">
							<ul class="pbmit-social-links">
								<li class="pbmit-social-li pbmit-social-facebook">
									<a title="Facebook" href="#" target="_blank">
										<span><i class="pbmit-base-icon-facebook-f"></i></span>
									</a>
								</li>
								<li class="pbmit-social-li pbmit-social-twitter">
									<a title="Twitter" href="#" target="_blank">
										<span><i class="pbmit-base-icon-twitter-2"></i></span>
									</a>
								</li>
								<li class="pbmit-social-li pbmit-social-linkedin">
									<a title="LinkedIn" href="#" target="_blank">
										<span><i class="pbmit-base-icon-linkedin-in"></i></span>
									</a>
								</li>
								<li class="pbmit-social-li pbmit-social-instagram">
									<a title="Instagram" href="#" target="_blank">
										<span><i class="pbmit-base-icon-instagram"></i></span>
									</a>
								</li>
							</ul>
						</div>
						<div class="pbmit-pre-header-right">
							<ul class="pbmit-contact-info">
								<li><i class="pbmit-base-icon-mail-alt"></i> <a
										href="#"
										class="__cf_email__"
										data-cfemail="#">intact999@gmail.com</a></li>
								<li><i class=" pbmit-base-icon-phone-volume-solid-1"></i>+91 1234567890</li>
							</ul>
						</div>
					</div>
				</div>
			</div>
			<div class="pbmit-main-header-area">
				<div class="container">
					<div class="pbmit-header-content d-flex justify-content-between align-items-center">
						<div class="pbmit-logo-area">
							<div class="site-branding">
								<h1 class="site-title">
									<a href="index.php">
										<img class="logo-img" src="images/intact-logo.png" alt="INTACT Design & Extrusion" style="max-height: 55px;">
									</a>
								</h1>
							</div>
						</div>
						<div class="site-navigation">
							<nav class="main-menu navbar-expand-xl navbar-light">
								<div class="navbar-header">
									<!-- Toggle Button -->
									<button class="navbar-toggler" type="button">
										<i class="pbmit-base-icon-menu-1"></i>
									</button>
								</div>
								<div class="pbmit-mobile-menu-bg"></div>
								<div class="collapse navbar-collapse clearfix show" id="pbmit-menu">
									<div class="pbmit-menu-wrap">
										<span class="closepanel">
											<svg class="qodef-svg--close qodef-m" xmlns="http://www.w3.org/2000/svg"
												width="20.163" height="20.163" viewBox="0 0 26.163 26.163">
												<rect width="36" height="1" transform="translate(0.707) rotate(45)">
												</rect>
												<rect width="36" height="1" transform="translate(0 25.456) rotate(-45)">
												</rect>
											</svg>
										</span>
										<?php $current_page = basename($_SERVER['PHP_SELF']); ?>
										<ul class="navigation clearfix">
											<li class="dropdown <?php echo ($current_page == 'ceiling.php') ? 'active' : ''; ?>">
												<a href="ceiling.php">CEILING</a>
												<ul>
													<li><a href="ceiling.php">PVC Ceiling Panels</a></li>
													<li><a href="ceiling.php#sub-categories">Plane PVC Panel</a></li>
													<li><a href="ceiling.php#sub-categories">SCIM 2 Grooves</a></li>
												</ul>
											</li>
											<li class="dropdown <?php echo ($current_page == 'walls.php') ? 'active' : ''; ?>">
												<a href="walls.php">WALLS</a>
												<ul>
													<li><a href="walls.php">PVC Wall Panels</a></li>
													<li><a href="walls.php#sub-categories">3G (3-Groove Fluted Panel)</a></li>
													<li><a href="walls.php#sub-categories">9G (9-Groove Fluted Panel)</a></li>
													<li><a href="walls.php#sub-categories">10G (10-Groove Fluted Panel)</a></li>
													<li><a href="walls.php#sub-categories">Sumo Panel</a></li>
												</ul>
											</li>
											<li class="<?php echo ($current_page == 'application.php') ? 'active' : ''; ?>">
												<a href="application.php">APPLICATION</a>
											</li>
											<li class="<?php echo ($current_page == 'quality.php') ? 'active' : ''; ?>">
												<a href="quality.php">QUALITY</a>
											</li>
											<li class="<?php echo ($current_page == 'about-us.php') ? 'active' : ''; ?>">
												<a href="about-us.php">ABOUT US</a>
											</li>
											<li class="dropdown <?php echo (in_array($current_page, ['downloads.php', 'installation-tips.php', 'cleaning-care-tips.php'])) ? 'active' : ''; ?>">
												<a href="#">RESOURCES</a>
												<ul>
													<li><a href="downloads.php">Downloads</a></li>
													<li><a href="installation-tips.php">Installation Tips</a></li>
													<li><a href="cleaning-care-tips.php">Cleaning and Care</a></li>
												</ul>
											</li>
											<li class="<?php echo ($current_page == 'contact-us.php') ? 'active' : ''; ?>">
												<a href="contact-us.php">CONTACT US</a>
											</li>
										</ul>
									</div>
								</div>
							</nav>
						</div>
						<div class="pbmit-right-box d-flex align-items-center">
							<div class="pbmit-button-box-second">
								<a class="pbmit-btn pbmit-btn-outline" href="#">
									<span class="pbmit-button-content-wrapper">
										<span class="pbmit-button-text">Explore Products</span>
									</span>
								</a>
							</div>
						</div>
					</div>
				</div>
			</div>
		</header>
		<!-- Header Main Area End Here -->