/*
** Copyright (C) 1998-2006 George Tzanetakis <gtzan@cs.uvic.ca>
**  
** This program is free software; you can redistribute it and/or modify
** it under the terms of the GNU General Public License as published by
** the Free Software Foundation; either version 2 of the License, or
** (at your option) any later version.
** 
** This program is distributed in the hope that it will be useful,
** but WITHOUT ANY WARRANTY; without even the implied warranty of
** MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
** GNU General Public License for more details.
** 
** You should have received a copy of the GNU General Public License
** along with this program; if not, write to the Free Software 
** Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
*/

/** 
    \class Peak2Rms
    \brief Multiply input realvec with Peak2Rms

   Simple MarSystem example. Just multiply the values of the input realvec
with Peak2Rms and put them in the output vector. This object can be used 
as a prototype template for building more complicated MarSystems. 
*/

#ifndef MARSYAS_PEAK2RMS_H
#define MARSYAS_PEAK2RMS_H

#include "MarSystem.h"	

namespace Marsyas
{

class Peak2Rms: public MarSystem
{

    public:
        Peak2Rms(std::string name);
        Peak2Rms(const Peak2Rms& a);
        ~Peak2Rms();
        MarSystem* clone() const;  

        void myUpdate();
        void myProcess(realvec& in, realvec& out);
};

}//namespace Marsyas

#endif
