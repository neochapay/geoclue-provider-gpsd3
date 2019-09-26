libexec_PROGRAMS = geoclue-gpsd3

geoclue_gpsd3_CFLAGS =	\
    $(GEOCLUE_CFLAGS) \
    $(GPSD_CFLAGS) 

geoclue_gpsd3_LDADD =		\
    $(GEOCLUE_LIBS)		\
    $(GPSD_LIBS)

geoclue_gpsd3_SOURCES =		\
    geoclue-gpsd3.c

providersdir = $(datadir)/geoclue-providers
providers_DATA = geoclue-gpsd3.provider

servicedir = $(DBUS_SERVICES_DIR)
service_in_files = org.freedesktop.Geoclue.Providers.Gpsd3.service.in
service_DATA = $(service_in_files:.service.in=.service)

$(service_DATA): $(service_in_files) Makefile
	$(AM_V_GEN) sed -e "s|\@libexecdir\@|$(libexecdir)|" $< > $@

EXTRA_DIST = 			\
    $(service_in_files)		\
    $(providers_DATA)

DISTCLEANFILES = 		\
    $(service_DATA)
