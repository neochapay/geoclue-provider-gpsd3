AC_INIT([geoclue-provider-gps3], [0.1], [https://neochapay.org])

AC_CONFIG_SRCDIR(src)
AM_INIT_AUTOMAKE
AC_PROG_CC
AC_PROG_INSTALL
AC_PROG_LIBTOOL

PKG_CHECK_MODULES(MASTER, [
		  libgps >= 3.19
		  geoclue >= 0.12.99
])

AC_SUBST(MASTER_LIBS)
AC_SUBST(MASTER_CFLAGS)

DBUS_SERVICES_DIR="${datadir}/dbus-1/services"
AC_SUBST(DBUS_SERVICES_DIR)
AC_DEFINE_UNQUOTED(DBUS_SERVICES_DIR, "$DBUS_SERVICES_DIR", [Where services dir for D-Bus is])

AC_OUTPUT(Makefile src/Makefile)
