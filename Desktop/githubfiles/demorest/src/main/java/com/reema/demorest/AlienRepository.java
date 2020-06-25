package com.reema.demorest;

import java.util.ArrayList;
import java.util.List;

public class AlienRepository
{
	List<Alien> aliens;
	
	public AlienRepository()
	{
		aliens=new ArrayList<Alien>();
		Alien a1=new Alien();
		a1.setName(" Reema");
		a1.setPoints(60);
		Alien a2=new Alien();
		a2.setName(" Ria");
		a2.setPoints(40);
		
		aliens.add(a1);
		aliens.add(a2);
	}

	public List<Alien> getAliens()
	{
		return aliens;
	}
	
	public Alien getAlien(int point)
	{
		
		for(Alien a:aliens)
		{
			if(a.getPoints()==point)
			{
				return a;
			}
		}
		return null;
	}

	public void create(Alien a1) {
		// TODO Auto-generated method stub
		aliens.add(a1);
	}
}
